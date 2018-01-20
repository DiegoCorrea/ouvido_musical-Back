from .algorithm import CosineSimilarity
from .models import CosineSimilarity_SongTitle
from apps.data.songs.models import Song, SongSimilarity
from apps.similarities.Cosine.benchmark.models import BenchCosine_SongTitle
from django.utils import timezone
from django.db import transaction

import logging
logger = logging.getLogger(__name__)


def saveTitleSimilarity(similarityMatrix, sBase, songInterator):
    for sComp in songInterator:
        SongSimilarity.objects.create(
            songBase=sBase['id'],
            songCompare=songInterator[sComp]['id'],
            similarity=similarityMatrix[sBase['position']][songInterator[sComp]['position']]
        )


def TitleSimilarity():
    logger.info("[Start Title Similarity]")
    allSongs = Song.objects.all()
    songPosition = {}
    line = 0
    similarityMatrix = CosineSimilarity([song.title for song in allSongs])
    for song in allSongs:
        songPosition.setdefault(song.id, {
            'id': song,
            'position': line
            }
        )
        line += 1
    # Persiste Title similarity
    logger.info("Start to persiste Title similarity")
    with transaction.atomic():
        for songBase in allSongs:
            sB = songPosition[songBase.id]
            del songPosition[songBase.id]
            logger.info("++ Song: " + str(sB['position']))
            saveTitleSimilarity(similarityMatrix, sB, songPosition)
    logger.info("[Finish Title Similarity]")


def runTitleSimilarity():
    logger.info("[Start Title Similarity with Cosine] - Benchmark")
    startedAt = timezone.now()
    TitleSimilarity()
    finishedAt = timezone.now()
    BenchCosine_SongTitle.objects.create(
        started_at=startedAt, finished_at=finishedAt
    )
    logger.info(
        "Benchmark: Start at - " + str(startedAt)
        + " || Finished at -" + str(finishedAt))
    logger.info("[Finish Title Similarity with Cosine] - Benchmark")
