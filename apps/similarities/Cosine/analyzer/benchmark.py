import matplotlib.pyplot as plt
import logging
import os

from random import sample
from django.utils import timezone
from apps.data.songs.models import Song

from apps.similarities.Cosine.algorithm.algorithm import CosineSimilarity
from apps.similarities.Cosine.benchmark.models import BenchCosine_SongTitle
from apps.similarities.Cosine.algorithm.models import CosineSimilarity_SongTitle

logger = logging.getLogger(__name__)


def runCosine(allSongs):
    startedAt = timezone.now()
    CosineSimilarity([song.title for song in allSongs])
    return timezone.now() - startedAt


def all_bench_gLine(size_list=[1500, 3000, 4500]):
    logger.info("[Start Bench Cosine (Graph Line)]")
    allBenchmarks = {}
    songs_list = Song.objects.all()
    for runner in size_list:
        if runner not in allBenchmarks:
            allBenchmarks.setdefault(runner, [])
        allBenchmarks[runner].append(
            (
                runCosine(allSongs=sample(set(songs_list), runner))
            ).total_seconds() / 60.0
        )
