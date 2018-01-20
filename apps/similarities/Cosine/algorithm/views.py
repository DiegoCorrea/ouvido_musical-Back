from .algorithm import CosineSimilarity
from .models import CosineSimilarity_SongTitle
from apps.data.songs.models import Song, SongSimilarity
from apps.similarities.Cosine.benchmark.models import BenchCosine_SongTitle
from django.utils import timezone
from django.db import transaction
from multiprocessing.dummy import Pool as ThreadPool

import logging
logger = logging.getLogger(__name__)

songInterator = {}
similarityMatrix = []


def saveTitleSimilarity(similarityMatrix, sBase, songInterator):
    for sComp in songInterator:
        SongSimilarity.objects.create(
            songBase=sBase['id'],
            songCompare=songInterator[sComp]['id'],
            similarity=similarityMatrix[sBase['position']][songInterator[sComp]['position']]
        )


def sstt(sBase):
    global similarityMatrix
    global songInterator
    logger.info("++ Song Title: " + str(songInterator[sBase]['id'].id))
    logger.info("++ Song Psition: " + str(songInterator[sBase]['position']))
    for sComp in songInterator:
        if(songInterator[sComp]['position'] < songInterator[sBase]['position']):
            continue
        SongSimilarity.objects.create(
            songBase=songInterator[sBase]['id'],
            songCompare=songInterator[sComp]['id'],
            similarity=similarityMatrix[songInterator[sBase]['position']][songInterator[sComp]['position']]
        )


def TitleSimilarity():
    logger.info("[Start Title Similarity]")
    global similarityMatrix
    global songInterator
    allSongs = Song.objects.all()
    line = 0
    similarityMatrix = CosineSimilarity([song.title for song in allSongs])
    for song in allSongs:
        songInterator.setdefault(song.id, {
            'id': song,
            'position': line
            }
        )
        line += 1
    # Persiste Title similarity
    logger.info("Start to persiste Title similarity")
    pool = ThreadPool(8)
    with transaction.atomic():
        pool.map(sstt, songInterator)
        pool.close()
        pool.join()
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
