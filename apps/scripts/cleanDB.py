from apps.data.songs.models import SongSimilarity
from apps.similarities.Cosine.algorithm.models import CosineSimilarity_SongTitle
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Recommendations
from apps.data.userSongRecommendation.models import UserSongRecommendations

def cleanDB(songSimi=True,cosSimi=True, userRec=True, userAveRec=True):
    if songSimi: SongSimilarity.objects.all().delete()
    if cosSimi: CosineSimilarity_SongTitle.objects.all().delete()
    if userRec: UserSongRecommendations.objects.all().delete()
    if userAveRec: UserAverage_Recommendations.objects.all().delete()

def cleanRecTables(userRec=True, userAveRec=True):
    if userRec: UserSongRecommendations.objects.all().delete()
    if userAveRec: UserAverage_Recommendations.objects.all().delete()
def cleanVotateTable():
    pass
