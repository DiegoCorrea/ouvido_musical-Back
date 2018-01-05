from collections import OrderedDict
from random import choice, randint
from api.users.models import User
from api.songs.models import Song
from api.userPlaySong.models import UserPlaySong
from api.userSongRecommendation.models import UserSongRecommendation
from api.benchmark.recommendators.models import UserAverage as benchUserAverage
from api.CONSTANTS import MAX_SCORE, MIN_SCORE
from time import gmtime, strftime
import logging
logger = logging.getLogger(__name__)

################################################################################
# User Average uses the average rating value of a user to make predictions.
#
def getUserAverageRecommendations(user_id):
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

def UserAverage():
    logger.info("[Start User Average]")
    for user in User.objects.all():
        userRecommendations = getUserAverageRecommendations(user.id)
        for (song, similarity) in userRecommendations.items():
            userRec = UserSongRecommendation(
                        song=Song.objects.get(id=song.id),
                        user_id=user.id,
                        similarity=similarity,
                        iLike=bool(choice([True, False])),
                        score=randint(MIN_SCORE,MAX_SCORE))
            userRec.save()
    logger.info("[Finish User Average]")

def runUserAverage():
    logger.info("[Start User Average - Benchmark]")
    execTime = [ ]
    execTime.append(strftime("%a, %d %b %Y %X", gmtime()))
    UserAverage()
    execTime.append(strftime("%a, %d %b %Y %X", gmtime()))
    bench = benchUserAverage(started_at=execTime[0],finished_at=execTime[1])
    bench.save()
    logger.info("Benchmark: Start at - ",execTime[0]," || Finished at -",execTime[1])
    logger.info("[Start User Average] - Benchmark")
################################################################################
