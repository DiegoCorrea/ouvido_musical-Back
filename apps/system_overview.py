from apps.data.users.models import User
from apps.data.songs.models import Song
from apps.data.userPlaySong.models import UserPlaySong
from django.db.models import Sum


def system_statistical():
    user_len = User.objects.count()
    heard_sum = UserPlaySong.objects.aggregate(Sum('play_count'))
    song_len = Song.objects.count()
    print('Heard : ' + str(heard_sum['play_count__sum']))
    print('+ Heard/User : ' + str(heard_sum['play_count__sum']/user_len))
    print('+ Heard/Song : ' + str(heard_sum['play_count__sum']/song_len))
