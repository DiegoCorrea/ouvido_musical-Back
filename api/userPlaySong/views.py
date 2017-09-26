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
from api.users.models import User
from .models import UserPlaySong
from .controllers import mostPlayedSongs

# Create your views here.

def mostPlayedSongsResource(request):
    if request.method == 'GET':
        try:
            results = [ob.as_json() for ob in mostPlayedSongs()]
            return HttpResponse(json.dumps(results), content_type="application/json")
        except Song.DoesNotExist:
            results = {}
            results['status'] = 404
            results['message'] = "Songs Not Found"
            return HttpResponse(json.dumps(results), content_type="application/json")
    else: # Qualquer coisa diferente de um GET eh probido e negado
        return HttpResponseForbidden()

def userSongs(request, user_id):
    objs = {}
    try:
        objs = UserPlaySong.objects.all().filter(user=user_id)[:20]
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
        objs = UserPlaySong.objects.all().filter(user_id=user_id, song_id=song_id)
    except UserPlaySong.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musica do Usuario não encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")
    results = [ob.as_json() for ob in objs]
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
    results = [ob.as_json() for ob in objs]
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
    results = [ob.as_json() for ob in objs]
    return HttpResponse(json.dumps(results), content_type="application/json")
