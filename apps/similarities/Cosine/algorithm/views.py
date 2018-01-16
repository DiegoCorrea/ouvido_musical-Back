from .algorithm import CosineSimilarity
from .models import CosineSimilarity_SongTitle
from apps.data.songs.models import Song, SongSimilarity
from apps.similarities.Cosine.benchmark.models import BenchCosine_SongTitle
from django.utils import timezone
from django.db import transaction

import logging
logger = logging.getLogger(__name__)
def TitleSimilarity():
    logger.info("[Start Title Similarity]")
    allSongs = Song.objects.all()
    bool(allSongs)
    similarSongs = { }
    newSongs = 0
    # Calc Cosine from Songs and return a symmetric matrix len(Songs) x len(Songs)
    similarityMatrix = CosineSimilarity([ song.title for song in allSongs ])
    # Load previous Songs similarities
    logger.info("Loading previous Songs similarities")
    for similar in SongSimilarity.objects.all():
        similarSongs.setdefault(similar.songBase_id, { })
        similarSongs[similar.songBase_id].setdefault(similar.songCompare_id, similar.similarity)
    # Persiste Title similarity
    logger.info("Start to persiste Title similarity")
    line = 0
    allHighSongs = allSongs
    with transaction.atomic():
        for songBase in allHighSongs:
            allSongs = allSongs.exclude(id=songBase.id)
            column = line + 1
            for songCompare in allSongs:
                SongSimilarity.objects.create(songBase=songBase, songCompare=songCompare, similarity=similarityMatrix[line][column])
                column += 1
            line += 1
    logger.debug("Total DB songs: %d", line)
    logger.info("[Finish Title Similarity]")
def runTitleSimilarity():
    logger.info("[Start Title Similarity with Cosine] - Benchmark")
    startedAt = timezone.now()
    TitleSimilarity()
    finishedAt = timezone.now()
    BenchCosine_SongTitle.objects.create(started_at=startedAt,finished_at=finishedAt)
    logger.info("Benchmark: Start at - " + str(startedAt) + " || Finished at -" + str(finishedAt))
    logger.info("[Finish Title Similarity with Cosine] - Benchmark")
