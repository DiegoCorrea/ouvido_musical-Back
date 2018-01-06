from .data.songs.models import SongSimilarity
from .similarities.Cosine.algorithm.models import CosineSimilarity_SongTitle
from .recommenders.UserAverage.algorithm.models import UserAverage_Recommendations

def cleanDB(songSimi=True,cosSimi=True, userRec=True):
    if songSimi: SongSimilarity.objects.all().delete()
    if cosSimi: CosineSimilarity_SongTitle.objects.all().delete()
    if userRec: UserAverage_Recommendations.objects.all().delete()
