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
    if request.method == 'GET':
        return JsonResponse({'status': 200, 'message': 'OK'})
    else: # Qualquer coisa diferente de um GET eh probido e negado
        return HttpResponseForbidden()

def mostPlayedSongs(request):
    if request.method == 'GET':
        objs = {}
        try:
            objs = UserPlaySong.objects.order_by('play_count').reverse()[:20]
            results = [ob.song.as_json() for ob in objs]
            return HttpResponse(json.dumps(results), content_type="application/json")
        except Song.DoesNotExist:
            results = {}
            results['status'] = 404
            results['message'] = "Songs Not Found"
            return HttpResponse(json.dumps(results), content_type="application/json")
    else: # Qualquer coisa diferente de um GET eh probido e negado
        return HttpResponseForbidden()

def song(request, song_id):
    if request.method == 'GET':
        ob = {}
        try:
            ob = Song.objects.get(id=song_id)
        except Song.DoesNotExist:
            results = {}
            results['status'] = 404
            results['message'] = "Song Not Found"
            return HttpResponse(json.dumps(results), content_type="application/json")
        results = [ob.as_json()]
        #dbpediaData = getFromDBpedia(ob.artist)
        #results.append(dbpediaData)
        return HttpResponse(json.dumps(results), content_type="application/json")
    else: # Qualquer coisa diferente de um GET eh probido e negado
        return HttpResponseForbidden()

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
