from collections import OrderedDict

from api.users.models import User
from api.songs.models import Song
from api.userPlaySong.models import UserPlaySong
from api.userSongRecommendation.models import UserSongRecommendation
from api.CONSTANTS import MAX_SCORE, MIN_SCORE

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

def makeUserRecommendation(DEBUG=1):
    status = 0
    users = User.objects.all()
    lenUsers = len(users)
    for user in users:
        recommendations = getUserRecommendations(user.id,DEBUG=DEBUG)
        # <DEBUG>
        if (DEBUG <= 1):
            status += 1
            print ('')
            print ("''"*30)
            print ('+ Progresso ', status, ' de ', lenUsers)
            print ('\nUser: ', user.id) # </DEBUG>
            print ('\nTotal de Recomendações ', len(recommendations))
        for (song_id, similarity) in recommendations.items():
            userRec = UserSongRecommendation(
                        song_id=song_id,
                        user_id=user.id,
                        similarity=similarity,
                        iLike=bool(choice([True, False])),
                        score=randint(MIN_SCORE,MAX_SCORE))
            userRec.save()
            # <DEBUG>
            if (DEBUG <= 2):
                song = Song.objects.get(id=song_id)
                print ('\n++++++++++++++++++++++++')
                print ('\t-- Musica: ', song.title)
                print ('\t-- Similaridade', similarity)
                print ('\t-- Like: ', userRec.iLike)
                print ('\t-- Score: ', userRec.score) # </DEBUG>
