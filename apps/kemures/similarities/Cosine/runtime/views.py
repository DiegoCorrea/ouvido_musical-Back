import logging

from random import sample
from django.utils import timezone
from apps.kemures.CONSTANTS import TOTAL_RUN, SET_SIZE_LIST
from apps.metadata.songs.models import Song
from apps.kemures.similarities.Cosine.algorithm import CosineSimilarity
from apps.kemures.similarities.Cosine.runtime import BenchCosine_SongTitle

logger = logging.getLogger(__name__)


def CosineBenchmark(allSongs):
    logger.info("[Start Bench Cosine]")
    startedAt = timezone.now()
    similarityMatrix = CosineSimilarity([song.title for song in allSongs])
    finishedAt = timezone.now()
    similaritySum = 0.0
    countTotal = 0.0
    for line in range(len(allSongs)):
        for column in range(line, len(allSongs)):
            countTotal += 1.0
            similaritySum += similarityMatrix[line][column]
    BenchCosine_SongTitle.objects.create(
        setSize=len(allSongs),
        similarity=(similaritySum/countTotal),
        started_at=startedAt,
        finished_at=finishedAt
    )
    logger.info("[Finish Bench Cosine]")


def RunCosineBenchmark(size_list=SET_SIZE_LIST):
    logger.info("[Start Run Bench Cosine]")
    songs_list = Song.objects.all()
    for runner in size_list:
        for i in range(TOTAL_RUN):
            logger.info(
                "\n#########################################################"
                + "\n\tTamanho do banco ("
                + str(runner)
                + ") Ciclo: "
                + str(i)
                + "\n#########################################################"
            )
            CosineBenchmark(allSongs=sample(set(songs_list), runner))
    logger.info("[Finish Run Bench Cosine]")
