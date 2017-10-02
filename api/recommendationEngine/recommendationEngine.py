from api.songs.models import Song, SongSimilarity
from api.users.models import User
from api.userPlaySong.models import UserPlaySong
from api.userSongRecommendation.models import UserSongRecommendation

from .songSimilarity import titleSimilarityAllDB
from .userRecommendation import getUserRecommendations

def runSimilarity():
    print("Iniciando o Calculo de Similaridade entre as Músicas")
    print("*** Etapa 1 - Titulos semelhantes ***")
    titleSimilarityAllDB()
    print("*** Calculo finalizao! ***")


def runUserRecommendation():
    for user in User.objects.all():
        recommendations = getUserRecommendations(user.id)
        for (song, similarity) in recommendations.items():
            userRec = UserSongRecommendation(song_id=song,user_id=user.id,probabilit_play_count=similarity,iLike=False)
            userRec.save()
