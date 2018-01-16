from collections import OrderedDict
from random import choice, randint, sample
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
def getUserAverageRecommendations(user_id, songSetLimit, songIDList):
    recommendation = { }
    songPlayedID_list = [ played.song_id for played in UserPlaySong.objects.filter(user_id=user_id)]
    songIDList = songIDList.exclude(songPlayedID_list)
    try:
        songIDList = sample(set(songIDList), songSetLimit)
    except ValueError as e:
        songIDList = sample(set(songIDList), len(songIDList))
    for songPlayed in userPlayed_list:
        for songSimi in songPlayed.song.getSimilaries(songIDList):
            if songSimi.similarity == 0.0: continue
            if songSimi.songCompare not in recommendation:
                recommendation.setdefault(songSimi.songCompare, [])
            recommendation[songSimi.songCompare].append(songSimi.similarity)
    rec = { }
    for (song, values) in recommendation.items():
        rec.setdefault(song, sum(values)/len(values))
    return OrderedDict(sorted(rec.items(), key=lambda t: t[1], reverse=True))
def UserAverage(userList=User.objects.all(), songSetLimit=Song.objects.count(), allSongs=Song.objects.all()):
    bool(allSongs)
    songIDList = [ song.id for song in allSongs ]
    UserAverage_Life.objects.create(setSize=songSetLimit)
    logger.info("[Start User Average]")
    with transaction.atomic():
        for user in userList:
            userRecommendations = getUserAverageRecommendations(user.id, songSetLimit, songIDList=songIDList)
            for (song, similarity) in userRecommendations.items():
                UserAverage_Recommendations.objects.create(
                            song=Song.objects.get(id=song.id),
                            user_id=user.id,
                            life = UserAverage_Life.objects.last(),
                            similarity=similarity,
                            iLike=bool(choice([True,False])),
                            score=randint(MIN_SCORE,MAX_SCORE))
    logger.info("[Finish User Average]")
