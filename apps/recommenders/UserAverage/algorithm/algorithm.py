from collections import OrderedDict
from random import choice, randint
from django.db import transaction

from apps.CONSTANTS import MAX_SCORE, MIN_SCORE
from apps.data.users.models import User
from apps.data.songs.models import Song
from apps.data.userPlaySong.models import UserPlaySong
from .models import UserAverage_Recommendations, UserAverage_Life

import logging
logger = logging.getLogger(__name__)
################################################################################
# User Average uses the average rating value of a user to make predictions.
#
def getUserAverageRecommendationsAllDB(user_id):
    recommendation = {}
    for songPlayed in UserPlaySong.objects.filter(user_id=user_id).order_by('play_count').reverse():
        for songSimi in songPlayed.song.getSimilaries():
            if songSimi.similarity == 0.0: continue
            if songSimi.songCompare not in recommendation:
                recommendation.setdefault(songSimi.songCompare, [])
            recommendation[songSimi.songCompare].append(songSimi.similarity)
    rec = {}
    for (song, values) in recommendation.items():
        rec.setdefault(song, sum(values)/len(values))
    return OrderedDict(sorted(rec.items(), key=lambda t: t[1], reverse=True))

def getUserAverageRecommendationsLimited(user_id, songSetLimit):
    recommendation = {}
    songIDList = [ song.id for song in Song.objects.all()[:songSetLimit]]
    for songPlayed in UserPlaySong.objects.filter(user_id=user_id).order_by('play_count').reverse():
        for songSimi in songPlayed.song.getSimilaries(songIDList):
            if songSimi.similarity == 0.0: continue
            if songSimi.songCompare not in recommendation:
                recommendation.setdefault(songSimi.songCompare, [])
            recommendation[songSimi.songCompare].append(songSimi.similarity)
    rec = {}
    for (song, values) in recommendation.items():
        rec.setdefault(song, sum(values)/len(values))
    return OrderedDict(sorted(rec.items(), key=lambda t: t[1], reverse=True))

def UserAverage(userList=User.objects.all(), songSetLimit=Song.objects.count()):
    logger.info("[Start User Average]")
    with transaction.atomic():
        for user in userList:
            userRecommendations = getUserAverageRecommendationsLimited(user.id, songSetLimit)
            for (song, similarity) in userRecommendations.items():
                userRec = UserAverage_Recommendations(
                            song=Song.objects.get(id=song.id),
                            user_id=user.id,
                            life = UserAverage_Life.objects.last().id,
                            similarity=similarity,
                            iLike=bool(choice([True,False])),
                            score=randint(MIN_SCORE,MAX_SCORE))
                userRec.save()
    logger.info("[Finish User Average]")
