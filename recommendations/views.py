# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.http import JsonResponse

from .models import Song
from .models import User
from .models import UserPlaySong
from .models import UserSongRecommendation

from .getDBpedia import getFromDBpedia

# Create your views here.
def index(request):
    return JsonResponse({'status': 200, 'message': 'Pagina inicial'})

def songs(request):
    try:
        #objs = Song.objects.all()
        results = [ob.as_json() for ob in Song.objects.order_by('song').filter()[:10]]
        return HttpResponse(json.dumps(results), content_type="application/json")
    except Song.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas nao encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")

def song(request, song_id):
    try:
        ob = Song.objects.get(song=song_id)
    except Song.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musica nao encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.as_json()]
    dbpediaData = getFromDBpedia(ob.artist)
    results.append(dbpediaData)
    return HttpResponse(json.dumps(results), content_type="application/json")

def songHearBy(request, song_id):
    try:
        objs = UserPlaySong.objects.all().filter(song=song_id)[0:10]
    except UserPlaySong.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas do Usuario não encontradas"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.user.as_json() for ob in objs]
    return HttpResponse(json.dumps(results), content_type="application/json")

def songHearByUser(request, song_id, user_id):
    try:
        objs = UserPlaySong.objects.all().filter(song=song_id,user=user_id)
    except UserPlaySong.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas do Usuario não encontradas"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.user.as_json() for ob in objs]
    return HttpResponse(json.dumps(results), content_type="application/json")


def users(request):
    try:
        results = [ob.as_json() for ob in User.objects.order_by('user').filter()[:10]]
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
    try:
        ob = User.objects.get(user=user_id)
    except User.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Usuario nao encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.as_json()]
    return HttpResponse(json.dumps(results), content_type="application/json")

def userSongs(request, user_id):
    try:
        objs = UserPlaySong.objects.all().filter(user=user_id)
    except UserPlaySong.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas do Usuario não encontradas"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.as_json() for ob in objs]
    return HttpResponse(json.dumps(results), content_type="application/json")

def userPlaySong(request, user_id, song_id):
    try:
        objs = UserPlaySong.objects.all().filter(user=user_id, song_id=song_id)
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
        objs = UserSongRecommendation.objects.all().filter(user=user_id)
    except UserSongRecommendation.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas Recomendadas para o Usuario não encontradas"
        return HttpResponse(json.dumps(results), content_type="application/json")
    rec = []
    for item in objs:
        rec.append(Song.objects.get(song=item.song_id))
    results = [ob.as_json() for ob in rec]
    print(results)
    return HttpResponse(json.dumps(results), content_type="application/json")
