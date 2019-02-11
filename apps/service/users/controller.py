from django.db.models import Sum
from django.http import HttpResponse, JsonResponse

from apps.metadata.user_preferences.models import UserPreference
from apps.metadata.users.models import User


def create():
    return JsonResponse({'message': "Create a user"})


def read(user_id):
    try:
        user = User.objects.get(id=user_id)
        user_preferences = UserPreference.objects.filter(user_id=user_id)
        songs_as_dict = {
            'id': user.id,
            'play_count': UserPreference.objects.filter(user_id=user_id).aggregate(Sum('play_count'))[
                'play_count__sum'],
            'users_preferences': user_preferences.count()
        }
        return JsonResponse(status=200, data=songs_as_dict)
    except Exception as e:
        return HttpResponse(str(e))


def update(user_id):
    return JsonResponse({'message': "Update a user"})


def delete(user_id):
    return JsonResponse({'message': "Delete a user"})


def all_songs():
    return JsonResponse({'message': "All user"})
