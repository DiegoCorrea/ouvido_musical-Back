from .algorithm import CosineSimilarity
from .models import CosineSimilarity_SongTitle
from apps.data.songs.models import Song, SongSimilarity
from django.utils import timezone
from django.db import transaction
from multiprocessing.dummy import Pool as ThreadPool
from apps.CONSTANTS import MAX_THREAD

import logging
logger = logging.getLogger(__name__)

songInterator = {}
similarityMatrix = []


def saveTitleSimilarity(sBase):
    global similarityMatrix
    global songInterator
    logger.info("++ Song Psition: " + str(songInterator[sBase]['pos']))
    for sComp in songInterator:
        if songInterator[sBase]['pos'] >= songInterator[sComp]['pos']:
            continue
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
