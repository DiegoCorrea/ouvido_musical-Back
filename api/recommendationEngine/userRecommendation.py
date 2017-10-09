from collections import OrderedDict

from api.songs.models import Song, SongSimilarity
from api.users.models import User
from api.userPlaySong.models import UserPlaySong

def getUserRecommendations(user_id, DEBUG=1):
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

def calcUserMAP(songRec, DEBUG=1):
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
        # <DEBUG>
        if (DEBUG != 0):
            print ('\t++ User MAP: ', sum(hitList)/relevant) # </DEBUG>
        return sum(hitList)/relevant
    else:
        # <DEBUG>
        if (DEBUG != 0):
            print ('\t++ User MAP: 0') # </DEBUG>
        return 0

def calcUserMRR(songRec, DEBUG=1):
    countDoc = 0
    for rec in songRec:
        countDoc += 1
        if (rec.iLike):
            # <DEBUG>
            if (DEBUG != 0):
                print ('\t++ MRR do usuario é: ', 1/countDoc) # </DEBUG>
            return 1/countDoc
    # <DEBUG>
    if (DEBUG != 0):
        print ('\t++ User MRR é: 0') # </DEBUG>
    return 0
