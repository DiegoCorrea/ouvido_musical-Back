from .models import UserPlaySong
from api.songs.models import Song
from api.users.models import User

from django.db.models import Avg
from django.db.models import Max
from django.db.models import Min
from django.db.models import Sum
from django.db.models import IntegerField
from django.db.models import Count

def allSongsAnalises():
    results = UserPlaySong.objects.aggregate(Avg('play_count'), Max('play_count'), Min('play_count'))
    songsTotalUserplay = Song.objects.annotate(totalUserPlayed=Count('userplaysong'), totalPlayed=Sum('userplaysong__play_count')).order_by('totalPlayed').reverse()
    return [
        results, songsTotalUserplay
    ]

def songAnalises(song_id):
    results = UserPlaySong.objects.filter(song=song_id).aggregate(Avg('play_count'), Max('play_count'), Min('play_count'), Sum('play_count'), Count('song'))
    return [
        results
    ]

def mostPlayedSongs(limit=10):
    return Song.objects.annotate(totalUserPlayed=Count('userplaysong'), totalPlayed=Sum('userplaysong__play_count')).order_by('totalPlayed').reverse()[0:limit]
