# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.http import JsonResponse

from .models import Song
from api.users.models import User
from api.users.models import UserPlaySong
from api.users.models import UserSongRecommendation
# Create your views here.
def index(request):
    return JsonResponse({'status': 200, 'message': 'Pagina inicial'})

def songs(request):
    objs = {}
    try:
        objs = UserPlaySong.objects.order_by('play_count').reverse()[:20]
        results = [ob.song.as_json() for ob in objs]
        return HttpResponse(json.dumps(results), content_type="application/json")
    except Song.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas nao encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")
        
def song(request, song_id):
    ob = {}
    try:
        ob = Song.objects.get(song=song_id)
    except Song.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musica nao encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.as_json()]
    #dbpediaData = getFromDBpedia(ob.artist)
    #results.append(dbpediaData)
    return HttpResponse(json.dumps(results), content_type="application/json")

def songHearBy(request, song_id):
    objs = {}
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
    objs = {}
    try:
        objs = UserPlaySong.objects.all().filter(song=song_id,user=user_id)
    except UserPlaySong.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas do Usuario não encontradas"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.user.as_json() for ob in objs]
    return HttpResponse(json.dumps(results), content_type="application/json")
