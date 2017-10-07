from collections import OrderedDict
import numpy as np
from sklearn.metrics import average_precision_score


from api.songs.models import Song, SongSimilarity
from api.users.models import User
from api.userPlaySong.models import UserPlaySong

def getUserRecommendations(user_id, DEBUG=0):
    hearSongs = UserPlaySong.objects.filter(user_id=user_id).order_by('play_count').reverse()
    recommendation = {}
    for songPlayed in hearSongs:
        similaries = songPlayed.song.songsimilarity_set.all()
        for songSimi in similaries:
            if songSimi.songCompare not in recommendation:
                recommendation.setdefault(songSimi.songCompare, [])
            recommendation[songSimi.songCompare].append(songSimi.similarity)
    rec = {}
    for (song, values) in recommendation.items():
        rec.setdefault(song, sum(values)/len(values))
    return OrderedDict(sorted(rec.items(), key=lambda t: t[1], reverse=True))

def calcUsersMAP(range=5, DEBUG=0):
    ap = [calcUserMAP(user.usersongrecommendation_set.all()[:range]) for user in User.objects.all()]

    if (DEBUG != 0):
        print('\n\tMean Averange Precision: ', np.mean(ap))


def calcUserMAP(songRec):
    hitList = []
    relevant = 0
    countDoc = 0
    for rec in songRec:
        countDoc += 1
        if (rec.iLike):
            relevant += 1
            hitList.append(relevant/countDoc)
    ap = sum(hitList)
    if (ap > 0):
        return sum(hitList)/relevant
    else:
        return 0
