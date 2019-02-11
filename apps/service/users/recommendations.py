from django.http import HttpResponse, JsonResponse

from apps.kemures.recommenders.UserAverage.DAO.models import UserAverageRecommendations


def index(user_id):
    try:
        user_recommendations = UserAverageRecommendations.objects.filter(user_id=user_id).order_by('-similarity')
        songs_as_dict = {}
        for recommendations in user_recommendations:
            songs_as_dict[str(recommendations.song_id)] = {
                'id': recommendations.song_id,
                'title': recommendations.song.title,
                'album': recommendations.song.album,
                'artist': recommendations.song.artist,
                'similarity': recommendations.similarity,
                'relevance_like': recommendations.relevance_like,
            }
        return JsonResponse(status=200, data=songs_as_dict)
    except Exception as e:
        return HttpResponse(str(e))


def update(user_id, song_id):
    return JsonResponse({'message': "Update a user"})
