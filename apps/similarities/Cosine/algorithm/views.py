from .algorithm import CosineSimilarity
from apps.data.songs.models import Song, SongSimilarity
from apps.similarities.Cosine.benchmark.models import BenchCosine_SongTitle
from django.db import transaction
from django.utils import timezone
from multiprocessing.dummy import Pool as ThreadPool
from apps.CONSTANTS import MAX_THREAD
from random import sample
import numpy as np

import logging
logger = logging.getLogger(__name__)

songInterator = {}
similarityMatrix = []


def saveTitleSimilarity(sBase):
    global similarityMatrix
    global songInterator
    logger.info("++ Song Psition: " + str(songInterator[sBase]['pos']))
    for sComp in songInterator[songInterator[sBase]['pos']:]:
        try:
            SongSimilarity.objects.create(
                songBase=songInterator[sBase]['obj'],
                songCompare=songInterator[sComp]['obj'],
                similarity=similarityMatrix[songInterator[sBase]['pos']][songInterator[sComp]['pos']]
            )
        except Exception:
            logger.info("-----Error Alert-----")
            continue


def TitleSimilarity():
    logger.info("[Start Title Similarity]")
    global similarityMatrix
    global songInterator
    allSongs = Song.objects.all()
    line = 0
    similarityMatrix = CosineSimilarity([song.title for song in allSongs])
    for song in allSongs:
        songInterator.setdefault(song.id, {
            'obj': song,
            'pos': line
            }
        )
        line += 1
    # Persiste Title similarity
    logger.info("Start to persiste Title similarity")
    pool = ThreadPool(MAX_THREAD)
    with transaction.atomic():
        pool.map(saveTitleSimilarity, songInterator)
        pool.close()
        pool.join()
    logger.info("[Finish Title Similarity]")


def TitleSimilarityWithObserver(setSize):
    logger.info("[Start Title Similarity]")
    allSongs = sample(set(Song.objects.all()), setSize)
    line = 0
    similarityVale = []
    startedAt = timezone.now()
    similarityMatrix = CosineSimilarity([song.title for song in allSongs])
    finishedAt = timezone.now()
    for i in range(len(allSongs)):
        for j in range(i, len(allSongs)):
            if j == i:
                continue
            line += 1
            similarityVale.append(similarityMatrix[i][j])
    BenchCosine_SongTitle.objects.create(
        setSize=setSize,
        similarity=np.mean(similarityVale),
        started_at=startedAt,
        finished_at=finishedAt
    )
    logger.info(
        "Benchmark: Start at - "
        + str(startedAt)
        + " || Finished at -"
        + str(finishedAt)
    )
