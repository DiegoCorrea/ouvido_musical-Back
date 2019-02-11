from django.http import HttpResponse, JsonResponse

from apps.metadata.user_preferences.models import UserPreference


def index(user_id):
    try:
        user_preferences = UserPreference.objects.filter(user_id=user_id)
        songs_as_dict = {}
        for preferences in user_preferences:
            songs_as_dict[str(preferences.song_id)] = {
                'id': preferences.song_id,
                'title': preferences.song.title,
                'album': preferences.song.album,
                'artist': preferences.song.artist,
                'play_count': preferences.play_count
            }
        return JsonResponse(status=200, data=songs_as_dict)
    except Exception as e:
        return HttpResponse(str(e))


def read(user_id, song_id):
    try:
        preferences = UserPreference.objects.get(user_id=user_id, song_id=song_id)
        songs_as_dict = {
            'id': preferences.song_id,
            'title': preferences.song.title,
            'album': preferences.song.album,
            'artist': preferences.song.artist,
            'play_count': preferences.play_count
        }
        return JsonResponse(status=200, data=songs_as_dict)
    except Exception as e:
        return HttpResponse(str(e))


def update(user_id, song_id):
    return JsonResponse({'message': "Update a user"})
