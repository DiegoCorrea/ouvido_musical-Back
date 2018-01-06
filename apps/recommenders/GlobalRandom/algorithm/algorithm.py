from collections import OrderedDict
from random import choice, randint, sample
from django.db import transaction

from apps.CONSTANTS import MAX_SCORE, MIN_SCORE
from apps.data.users.models import User
from apps.data.songs.models import Song
from apps.data.userPlaySong.models import UserPlaySong
from apps.similarities.Cosine.algorithm.algorithm import CosineSimilarity
from .models import GlobalRandom_Recommendations

import logging
logger = logging.getLogger(__name__)
################################################################################
def randomCosineTitle(qtde=50):
    sample = sample(xrange(Song.objects.count()),qtde)
    allSongs = [Song.objects.all()[i] for i in sample]
    similarList = [ ]
    similarSongs = { }
    similarityMatrix = CosineSimilarity([ song.title for song in allSongs ])
    for songBase in allSongs:
        allSongs = allSongs.exclude(id=songBase.id)
        if (songBase.id not in similarSongs):
            similarSongs.setdefault(songBase.id, { })
            newSongs += 1
        j = i + 1
        for songCompare in allSongs:
            if (((songBase.id in similarSongs) and (songCompare.id in similarSongs[songBase.id])) or ((songCompare.id in similarSongs) and (songBase.id in similarSongs[songCompare.id]))):
                continue
            similarList.append(SongSimilarity(songBase=songBase, songCompare=songCompare, similarity=similarityMatrix[i][j]))
            j += 1
        i += 1
    return similarList
################################################################################
# User Average uses the average rating value of a user to make predictions.
#
def getGlobalRandomRecommendations(user_id):
    recommendation = {}
    for songPlayed in UserPlaySong.objects.all().order_by('play_count').reverse():
        for songSimi in randomCosineTitle():
            if songSimi.similarity == 0.0: continue
            if songSimi.songCompare not in recommendation:
                recommendation.setdefault(songSimi.songCompare, [])
            recommendation[songSimi.songCompare].append(songSimi.similarity)
    rec = {}
    for (song, values) in recommendation.items():
        rec.setdefault(song, sum(values)/len(values))
    return OrderedDict(sorted(rec.items(), key=lambda t: t[1], reverse=True))

def GlobalRandom():
    logger.info("[Start Global Random]")
    with transaction.atomic():
        for user in User.objects.all():
            userRecommendations = getGlobalRandomRecommendations()
            for (song, similarity) in userRecommendations.items():
                userRec = GlobalRandom_Recommendations(
                            song=Song.objects.get(id=song.id),
                            user_id=user.id,
                            similarity=similarity,
                            iLike=bool(choice([True, False])),
                            score=randint(MIN_SCORE,MAX_SCORE))
                userRec.save()
    logger.info("[Finish Global Random]")
