from api.songs.models import Song, SongSimilarity
from .similarityAlgorithms import cosineSimilarity
import logging
logger = logging.getLogger(__name__)
def TitleSimilarity():
    logger.info("[Start Title Similarity]")
    allSongs = Song.objects.all()
    similarSongs = { }
    newSongs = 0
    # Calc Cosine from Songs and return a symmetric matrix len(Songs) x len(Songs)
    similarityMatrix = cosineSimilarity([ song.title for song in allSongs ])
    # Load previous Songs similarities
    logger.info("Loading previous Songs similarities")
    for similar in SongSimilarity.objects.all():
        similarSongs.setdefault(similar.songBase_id, { })
        similarSongs[similar.songBase_id].setdefault(similar.songCompare_id, similar.similarity)
    # Persiste Title similarity
    logger.info("Start to persiste Title similarity")
    i = 0
    for songBase in allSongs:
        allSongs = allSongs.exclude(id=songBase.id)
        if (songBase.id not in similarSongs):
            similarSongs.setdefault(songBase.id, { })
            newSongs += 1
        j = i + 1
        for songCompare in allSongs:
            if (((songBase.id in similarSongs) and (songCompare.id in similarSongs[songBase.id])) or ((songCompare.id in similarSongs) and (songBase.id in similarSongs[songCompare.id]))):
                continue
            similar = SongSimilarity(songBase=songBase, songCompare=songCompare, similarity=similarityMatrix[i][j])
            similar.save()
            j += 1
        i += 1
    logger.debug("Total DB songs: %d", i)
    logger.debug("Total new songs: %d", newSongs-1)
    logger.info("[Finish Title Similarity]")
