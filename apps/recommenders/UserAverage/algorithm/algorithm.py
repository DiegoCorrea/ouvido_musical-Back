from collections import OrderedDict
from random import choice, randint, sample
from django.db import transaction
from multiprocessing.dummy import Pool as ThreadPool

from apps.CONSTANTS import MAX_SCORE, MIN_SCORE, MAX_THREAD
from apps.data.users.models import User
from apps.data.songs.models import Song
from apps.data.userPlaySong.models import UserPlaySong
from .models import UserAverage_Recommendations, UserAverage_Life

import copy
import logging
logger = logging.getLogger(__name__)

SONGSET_LIMIT = 0
SONGDB_IDS = None


def setSongLimitOnMap(songSetLimit):
    global SONGSET_LIMIT
    SONGSET_LIMIT = songSetLimit


def setAllSongsIdOnMemory():
    global SONGDB_IDS
    SONGDB_IDS = [song.id for song in Song.objects.all()]


def getUserAverageRecommendations(user):
    logger.info("[Start Get User Recommendation] - id: " + str(user.id))
    global SONGDB_IDS
    recommendations = {}
    userModel = []
    songs_ids_list = copy.deepcopy(SONGDB_IDS)
    userPlayed_list = UserPlaySong.objects.filter(user_id=user.id)
    for played in userPlayed_list:
        songs_ids_list.remove(played.song_id)
    try:
        userModel = sample(set(songs_ids_list), SONGSET_LIMIT)
    except ValueError:
        userModel = sample(set(songs_ids_list), len(songs_ids_list))
    for songPlayed in userPlayed_list:
        similaresSide = songPlayed.song.getSimilaries(songIDList=userModel)
        for songSimi in similaresSide:
            if songSimi.similarity == 0.0:
                continue
            if songSimi.songCompare in recommendations:
                recommendations[songSimi.songCompare].append(songSimi.similarity)
                continue
            if songSimi.songBase in recommendations:
                recommendations[songSimi.songBase].append(songSimi.similarity)
                continue
            if songSimi.songCompare is not songPlayed.song and songSimi.songCompare not in recommendations:
                recommendations.setdefault(songSimi.songCompare, [])
                recommendations[songSimi.songCompare].append(songSimi.similarity)
                continue
            if songSimi.songBase is not songPlayed.song and songSimi.songBase not in recommendations:
                recommendations.setdefault(songSimi.songBase, [])
                recommendations[songSimi.songBase].append(songSimi.similarity)
                continue
    rec = {}
    for (song, values) in recommendations.items():
        rec.setdefault(song, sum(values)/len(values))
    with transaction.atomic():
        for (song, similarity) in OrderedDict(sorted(rec.items(), key=lambda t: t[1], reverse=True)).items():
            try:
                UserAverage_Recommendations.objects.create(
                        song_id=song.id,
                        user_id=user.id,
                        life_id=UserAverage_Life.objects.last().id,
                        similarity=similarity,
                        iLike=bool(choice([True, False])),
                        score=randint(MIN_SCORE, MAX_SCORE))
            except Exception:
                logger.info("-----Error Alert-----")
                continue


def UserAverage(songSetLimit=Song.objects.count()):
    logger.info("[Start User Average]")
    UserAverage_Life.objects.create(setSize=songSetLimit)
    setSongLimitOnMap(songSetLimit=songSetLimit)
    setAllSongsIdOnMemory()
    userList = User.objects.all()
    pool = ThreadPool(MAX_THREAD)
    pool.map(getUserAverageRecommendations, userList)
    pool.close()
    pool.join()
    logger.info("[Finish User Average]")
