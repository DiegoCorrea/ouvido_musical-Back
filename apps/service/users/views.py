from django.http import JsonResponse

from .controller import create, read, update, delete, all_songs
from .songs import index as song_index, read as read_a_user_song, update as update_a_user_song


def index(request):
    if request.method == 'GET':
        return all_songs()
    elif request.method == 'PUT':
        return create()
    return JsonResponse({'message': 'Não utilizamos este tipo de requisição'})


def process_request(request, user_id=''):
    if request.method == 'GET':
        return read(user_id)
    elif request.method == 'POST':
        return update(user_id)
    elif request.method == 'DELETE':
        return delete(user_id)
    return JsonResponse({'message': 'Não utilizamos este tipo de requisição'})


def index_song_request(request, user_id=''):
    if request.method == 'GET':
        return song_index(user_id)
    elif request.method == 'PUT':
        return create()
    return JsonResponse({'message': 'Não utilizamos este tipo de requisição'})


def song_request(request, user_id, song_id):
    if request.method == 'GET':
        return read_a_user_song(user_id, song_id)
    elif request.method == 'POST':
        return update_a_user_song(user_id, song_id)
    return JsonResponse({'message': 'song request'})
