from collections import OrderedDict
from random import choice, randint
from api.users.models import User
from api.songs.models import Song
from api.userPlaySong.models import UserPlaySong
from api.userSongRecommendation.models import UserSongRecommendation

from apps.recommenders.UserAverage.benchmark.models import benchUserAverage
from apps.CONSTANTS import MAX_SCORE, MIN_SCORE
from django.utils import timezone
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
    startAt = timezone.now()
    UserAverage()
    bench = benchUserAverage(started_at=startAt,finished_at=timezone.now())
    bench.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    logger.info("[Start User Average] - Benchmark")
