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


def getUserAverageRecommendations(user_id, songSetLimit, songIDList):
    recommendation = {}
    userPlayed_list = UserPlaySong.objects.filter(user_id=user_id)
    for played in userPlayed_list:
        songIDList.remove(played.song_id)
    try:
        songIDList = sample(set(songIDList), songSetLimit)
    except ValueError:
        songIDList = sample(set(songIDList), len(songIDList))
    for songPlayed in userPlayed_list:
        print("aaa")
        print (str(len(songIDList)))
        similaresSide = songPlayed.song.getSimilaries(set(songIDList))
        print("!!!! "+str(len(similaresSide)))
        for songSimi in similaresSide:
            # if songSimi.similarity == 0.0: continue
            if songSimi.songCompare not in recommendation:
                recommendation.setdefault(songSimi.songCompare, [])
            recommendation[songSimi.songCompare].append(songSimi.similarity)
    rec = {}
    for (song, values) in recommendation.items():
        rec.setdefault(song, sum(values)/len(values))
    return OrderedDict(sorted(rec.items(), key=lambda t: t[1], reverse=True))


def UserAverage(userList=User.objects.all(), songSetLimit=Song.objects.count(), allSongs=Song.objects.all()):
    bool(allSongs)
    songIDList = [song.id for song in allSongs]
    UserAverage_Life.objects.create(setSize=songSetLimit)
    logger.info("[Start User Average]")
    with transaction.atomic():
        for user in userList:
            userRecommendations = getUserAverageRecommendations(user.id, songSetLimit, set(songIDList))
            print("---+++ "+str(len(userRecommendations)))
            for (song, similarity) in userRecommendations.items():
                UserAverage_Recommendations.objects.create(
                            song=Song.objects.get(id=song.id),
                            user_id=user.id,
                            life=UserAverage_Life.objects.last().id,
                            similarity=similarity,
                            iLike=bool(choice([True,False])),
                            score=randint(MIN_SCORE,MAX_SCORE))
    logger.info("[Finish User Average]")


# ###############################################################################
SONGSET_LIMIT = 0
SONGDB_IDS = None


def setSongLimitOnMap(songSetLimit):
    global SONGSET_LIMIT
    SONGSET_LIMIT = songSetLimit


def setAllSongsIdOnMemory():
    global SONGDB_IDS
    SONGDB_IDS = [song.id for song in Song.objects.all()]


def getUserAverageRecommendations_b(user):
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
            # if songSimi.similarity == 0.0:
            #    continue
            if songSimi.songCompare not in recommendations:
                recommendations.setdefault(songSimi.songCompare, [])
            recommendations[songSimi.songCompare].append(songSimi.similarity)
    rec = {}
    for (song, values) in recommendations.items():
        rec.setdefault(song, sum(values)/len(values))
    with transaction.atomic():
        for (song, similarity) in OrderedDict(sorted(rec.items(), key=lambda t: t[1], reverse=True)).items():
            UserAverage_Recommendations.objects.create(
                        song_id=song.id,
                        user_id=user.id,
                        life_id=UserAverage_Life.objects.last().id,
                        similarity=similarity,
                        iLike=bool(choice([True, False])),
                        score=randint(MIN_SCORE, MAX_SCORE))


def UserAverage_n(songSetLimit=Song.objects.count()):
    logger.info("[Start User Average]")
    setSongLimitOnMap(songSetLimit=songSetLimit)
    setAllSongsIdOnMemory()
    userList = User.objects.all()
    UserAverage_Life.objects.create(setSize=songSetLimit)
    pool = ThreadPool(MAX_THREAD)
    pool.map(getUserAverageRecommendations_b, userList)
    pool.close()
    pool.join()
    logger.info("[Finish User Average]")
