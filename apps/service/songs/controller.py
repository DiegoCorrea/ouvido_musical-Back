from django.db.models import Sum
from django.http import HttpResponse, JsonResponse

from apps.metadata.songs.models import Song
from apps.metadata.user_preferences.models import UserPreference


def create():
    return JsonResponse({'message': "Create a song"})


def read(song_id):
    try:
        song = Song.objects.get(id=song_id)
        user_preferences = UserPreference.objects.filter(song_id=song_id)
        songs_as_dict = {
            'id': song.id,
            'title': song.title,
            'album': song.album,
            'artist': song.artist,
            'play_count': UserPreference.objects.filter(song_id=song_id).aggregate(Sum('play_count'))[
                'play_count__sum'],
            'users_preferences': user_preferences.count()
        }
        return JsonResponse(status=200, data=songs_as_dict)
    except Exception as e:
        return HttpResponse(str(e))


def update(song_id):
    return JsonResponse({'message': "Update a song"})


def delete(song_id):
    return JsonResponse({'message': "Delete a song"})


def all_songs():
    return JsonResponse({'message': "All songs"})
