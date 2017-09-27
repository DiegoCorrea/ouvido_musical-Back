from api.songs.models import Song, SongSimilarity
from api.users.models import User
from api.userPlaySong.models import UserPlaySong

def getUserRecommenations(user_id):
    user = User.objects.get(id=user_id)
    hearSongs = UserPlaySong.objects.filter(user_id=user_id).order_by('play_count').reverse()
    for song in hearSongs[10]
        similaries = Song.SongSimilarity.get(id=song.id)
