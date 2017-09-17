# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.http import JsonResponse

from api.songs.models import Song
from .models import User
from .models import UserPlaySong
from .models import UserSongRecommendation

# Create your views here.

def index(request):
    return JsonResponse({'status': 200, 'message': 'Home'})

def users(request):
    results = {}
    try:
        results = [ob.as_json() for ob in User.objects.all().order_by('id')[:10]]
        return HttpResponse(json.dumps(results), content_type="application/json")
    except User.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Usuarios nao encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results['status'] = 500
    results['message'] = "Deu merda!"
    return HttpResponse(json.dumps(results), content_type="application/json")

def user(request, user_id):
    ob = {}
    try:
        ob = User.objects.get(id=user_id)
    except User.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Usuario nao encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.as_json()]
    return HttpResponse(json.dumps(results), content_type="application/json")

def userSongs(request, user_id):
    objs = {}
    try:
        objs = UserPlaySong.objects.all().filter(id=user_id)
    except UserPlaySong.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas do Usuario não encontradas"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.as_json() for ob in objs]
    return HttpResponse(json.dumps(results), content_type="application/json")

def userPlaySong(request, user_id, song_id):
    objs = {}
    try:
        objs = UserPlaySong.objects.all().filter(id=user_id, song_id=song_id)
    except UserPlaySong.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musica do Usuario não encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.as_json() for ob in objs]
    return HttpResponse(json.dumps(results), content_type="application/json")

def userSimilarity(request, user_id):
    objs = {}
    try:
        objs = UserSongRecommendation.objects.all().filter(id=user_id).order_by('probabilit_play_count').reverse()[:10]
    except UserSongRecommendation.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas Recomendadas para o Usuario não encontradas"
        return HttpResponse(json.dumps(results), content_type="application/json")
    rec = []
    for item in objs:
        rec.append(Song.objects.get(id=item.song_id))
    results = [ob.as_json() for ob in rec]
    return HttpResponse(json.dumps(results), content_type="application/json")

@csrf_exempt
def UserMusicRecommendation(request, user_id, song_id):
    if request.method == 'GET':
        obj = {}
        try:
            obj = UserSongRecommendation.objects.get(id=user_id, song_id=song_id)
        except UserSongRecommendation.DoesNotExist:
            results = {}
            results['status'] = 404
            results['message'] = "Musicas Recomendadas para o Usuario não encontradas"
            return HttpResponse(json.dumps(results), content_type="application/json")
        return HttpResponse(json.dumps(obj.as_json()), content_type="application/json")
    elif request.method == 'POST':
        musicRecommendation = UserSongRecommendation.objects.get(user=user_id, song_id=song_id)
        received_json_data = json.loads(request.body.decode("utf-8"))
        print (received_json_data)

        if received_json_data['iLike']:
            musicRecommendation.iLike = received_json_data['iLike']
            musicRecommendation.save()
            print(musicRecommendation)
        results = {}
        results['status'] = 200
        results['message'] = "Musicas Recomendadas para o Usuario"
        return HttpResponse(json.dumps(results), content_type="application/json")

@csrf_exempt
def UserLikeMusicRecommendation(request, user_id, song_id):
    print("Entrando em Curtir")
    if request.method == 'GET':
        try:
            obj = {}
            result = {}
            obj = UserSongRecommendation.objects.get(id=user_id, song_id=song_id)
            result['iLike'] = obj.iLike
            return HttpResponse(json.dumps(result), content_type="application/json")
        except UserSongRecommendation.DoesNotExist:
            results = {}
            results['status'] = 404
            results['message'] = "Musicas Recomendadas para o Usuario não encontradas"
            return HttpResponse(json.dumps(results), content_type="application/json")
    elif request.method == 'POST':
        musicRecommendation = UserSongRecommendation.objects.get(user=user_id, song_id=song_id)
        received_json_data = json.loads(request.body.decode("utf-8"))
        print (received_json_data)

        musicRecommendation.iLike = received_json_data['iLike']
        musicRecommendation.save()
        print(musicRecommendation)
        results = {}
        results['status'] = 200
        results['message'] = "Salvo com Sucesso"
        return HttpResponse(json.dumps(results), content_type="application/json")
