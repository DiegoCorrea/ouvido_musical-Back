import matplotlib.pyplot as plt
import logging
import os

from random import sample
from django.utils import timezone
from apps.data.songs.models import Song
from apps.similarities.Cosine.algorithm.algorithm import CosineSimilarity
from apps.similarities.Cosine.benchmark.models import BenchCosine_SongTitle

logger = logging.getLogger(__name__)


def CosineBenchmark(allSongs):
    logger.info("[Start Bench Cosine]")
    startedAt = timezone.now()
    CosineSimilarity([song.title for song in allSongs])
    BenchCosine_SongTitle.objects.create(
        setSize=len(allSongs),
        started_at=startedAt,
        finished_at=timezone.now()
    )
    logger.info("[Finish Bench Cosine]")


def RunCosineBenchmark(size_list=[1500, 3000, 4500]):
    logger.info("[Start Run Bench Cosine]")
    songs_list = Song.objects.all()
    for runner in size_list:
        for i in range(10):
            logger.info(
                "\tTamanho do banco ("
                + str(runner)
                + ") Ciclo: "
                + str(i)
            )
            CosineBenchmark(allSongs=sample(set(songs_list), runner))
    logger.info("[Finish Run Bench Cosine]")
