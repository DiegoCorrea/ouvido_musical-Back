from django.http import JsonResponse

from .controller import create, read, update, delete, all_songs


def index(request):
    if request.method == 'GET':
        return all_songs()
    elif request.method == 'PUT':
        return create()
    return JsonResponse({'message': 'Não utilizamos este tipo de requisição'})


def process_request(request, song_id=''):
    if request.method == 'GET':
        return read(song_id)
    elif request.method == 'POST':
        return update(song_id)
    elif request.method == 'DELETE':
        return delete(song_id)
    return JsonResponse({'message': 'Não utilizamos este tipo de requisição'})
