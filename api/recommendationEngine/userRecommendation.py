from collections import OrderedDict

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
