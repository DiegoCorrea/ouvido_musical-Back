from random import choice, randint, sample
from django.db import transaction

from django.db.models import Sum
from multiprocessing.dummy import Pool as ThreadPool

from apps.metadata.CONSTANTS import (
    MAX_SCORE,
    MIN_SCORE,
    MAX_THREAD,
    RECOMMENDATION_LIMIT
)
from apps.metadata.users.models import User
from apps.metadata.songs.models import Song
from apps.metadata.user_preferences.models import UserPlaySong
from .models import UserAverage_Recommendations, UserAverage_Life

import copy
import logging
logger = logging.getLogger(__name__)

RECOMMENDATION_CONFIG = {
    'SONGSET_LIMIT': 0,
    'LIFE_ID': None,
    'SONGDB_IDS': []
}


def createUserModel(userPlayed_list):
    songs_ids_list = copy.deepcopy(RECOMMENDATION_CONFIG['SONGDB_IDS'])
    for played in userPlayed_list:
        songs_ids_list.remove(played.song_id)
    try:
        return sample(set(songs_ids_list), RECOMMENDATION_CONFIG['SONGSET_LIMIT'])
    except ValueError:
        return sample(set(songs_ids_list), len(songs_ids_list))


def getUserAverageRecommendations(user):
    logger.info("[Start Get User Recommendation] - id: " + str(user.id))
    global SONGDB_IDS
    recommendations = {}
    userModel = None
    #
    userPlayed_list = UserPlaySong.objects.filter(user_id=user.id)
    userModel = createUserModel(userPlayed_list=userPlayed_list)
    for songPlayed in userPlayed_list:
        similaresSide = songPlayed.song.getSimilaries(songIDList=userModel)
        for songSimi in similaresSide:
            if songSimi.similarity == 0.0:
                continue
            if songSimi.songBase == songPlayed.song:
                if songSimi.songCompare in recommendations:
                    recommendations[songSimi.songCompare].append(
                        songSimi.similarity
                    )
                else:
                    recommendations.setdefault(songSimi.songCompare, [])
                    recommendations[songSimi.songCompare].append(
                        songSimi.similarity
                    )
            else:
                if songSimi.songBase in recommendations:
                    recommendations[songSimi.songBase].append(
                        songSimi.similarity
                    )
                else:
                    recommendations.setdefault(songSimi.songBase, [])
                    recommendations[songSimi.songBase].append(
                        songSimi.similarity
                    )
    rec = {}
    for (song, values) in recommendations.items():
        rec.setdefault(song, sum(values)/len(values))
    orderedRecomendation = sorted(
                                rec.items(),
                                key=lambda t: t[1],
                                reverse=True
                            )[:RECOMMENDATION_LIMIT]
    with transaction.atomic():
        for (song, similarity) in orderedRecomendation:
            try:
                UserAverage_Recommendations.objects.create(
                        song_id=song.id,
                        user_id=user.id,
                        life_id=RECOMMENDATION_CONFIG['LIFE_ID'],
                        similarity=similarity,
                        iLike=bool(choice([True, False])),
                        score=randint(MIN_SCORE, MAX_SCORE))
            except Exception as e:
                logger.error(str(e))
                continue


def UserAverage(songSetLimit=Song.objects.count()):
    global RECOMMENDATION_CONFIG
    logger.info("[Start User Average]")
    life = UserAverage_Life.objects.create(setSize=songSetLimit)
    RECOMMENDATION_CONFIG['SONGSET_LIMIT'] = songSetLimit
    RECOMMENDATION_CONFIG['SONGDB_IDS'] = [song.id for song in Song.objects.all()]
    RECOMMENDATION_CONFIG['LIFE_ID'] = life.id
    userList = User.objects.all()
    pool = ThreadPool(MAX_THREAD)
    pool.map(getUserAverageRecommendations, userList)
    pool.close()
    pool.join()
    life.length = UserAverage_Recommendations.objects.count()
    life.similarity = UserAverage_Recommendations.objects.aggregate(
            Sum('similarity')
        )['similarity__sum']/life.length
    life.score = UserAverage_Recommendations.objects.aggregate(
            Sum('score')
        )['score__sum']/life.length
    life.save()
    logger.info("[Finish User Average]")
