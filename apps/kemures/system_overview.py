from apps.metadata.users.models import User
from apps.metadata.songs.models import Song
from apps.metadata.user_preferences.models import UserPlaySong
from apps.kemures.similarities.Cosine.runtime import BenchCosine_SongTitle
from apps.kemures.recommenders.UserAverage import UserAverage_Life
from django.db.models import Sum

from apps.kemures.CONSTANTS import SET_SIZE_LIST, START_VALIDE_RUN, TOTAL_RUN, INTERVAL


def system_statistical():
    user_len = User.objects.count()
    heard_sum = UserPlaySong.objects.aggregate(Sum('play_count'))
    song_len = Song.objects.count()
    print('Heard : ' + str(heard_sum['play_count__sum']))
    print('+ Heard/User : ' + str(heard_sum['play_count__sum']/user_len))
    print('+ Heard/Song : ' + str(heard_sum['play_count__sum']/song_len))


def cosine_overview():
    print('Similarities')
    meanSimilarities = {}
    for size in SET_SIZE_LIST:
        meanSimilarities[size] = BenchCosine_SongTitle.objects.filter(setSize=size)[START_VALIDE_RUN:TOTAL_RUN].aggregate(total=Sum('similarity'))['total']/INTERVAL
        print(str(size) + ': ' + str(meanSimilarities[size]))
    print('Time Latency')
    allBenchmarks = {}
    for runner in SET_SIZE_LIST:
        allBenchmarks.setdefault(runner, [])
        for benchmark in BenchCosine_SongTitle.objects.filter(
            setSize=runner
        )[START_VALIDE_RUN:TOTAL_RUN]:
            allBenchmarks[runner].append(
                (
                    benchmark.finished_at - benchmark.started_at
                ).total_seconds()
            )
        print(str(runner) + ': ' + str(sum(allBenchmarks[runner])/INTERVAL))


def userAverage_overview():
    print('Similarities')
    meanSimilarities = {}
    for size in SET_SIZE_LIST:
        meanSimilarities[size] = UserAverage_Life.objects.filter(setSize=size).order_by('-id')[:INTERVAL].aggregate(total=Sum('similarity'))['total']/INTERVAL
        print(str(size) + ': ' + str(meanSimilarities[size]))
    print('Time Latency')
    allBenchmarks = {}
    for runner in SET_SIZE_LIST:
        allBenchmarks.setdefault(runner, [])
        for benchmark in UserAverage_Life.objects.filter(
            setSize=runner
        ):
            allBenchmarks[runner].append(
                (
                    benchmark.benchuseraverage.finished_at - benchmark.benchuseraverage.started_at
                ).total_seconds()
            )
        print(str(runner) + ': ' + str(sum(allBenchmarks[runner][-INTERVAL:])/INTERVAL))
