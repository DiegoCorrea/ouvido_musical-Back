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
from .models import SongSimilarity

# Create your views here.
def index(request):
    if request.method == 'GET':
        return JsonResponse({'status': 200, 'message': 'OK'})
    else: # Qualquer coisa diferente de um GET eh probido e negado
        return HttpResponseForbidden()

def allSongs(request):
    objs = {}
    try:
        objs = Song.objects.all()[:20]
        results = [ob.as_json() for ob in objs]
        return HttpResponse(json.dumps(results), content_type="application/json")
    except Song.DoesNotExist:
        results = {}
        results['status'] = 404
        results['message'] = "Musicas nao encontrada"
        return HttpResponse(json.dumps(results), content_type="application/json")

def song(request, song_id):
    if request.method == 'GET':
        ob = {}
        try:
            ob = Song.objects.get(id=song_id)
        except Song.DoesNotExist:
            results = {}
            results['status'] = 404
            results['message'] = "Song Not Found"
            return HttpResponseNotFound(HttpResponse(json.dumps(results), content_type="application/json"))
        results = [ob.as_json()]
        return HttpResponse(json.dumps(results), content_type="application/json")
    else: # Qualquer coisa diferente de um GET eh probido e negado
        return HttpResponseForbidden()

def songSimilares(request, song_id):
    if request.method == 'GET':
        objs = {}
        try:
            objs = SongSimilarity.objects.all().filter(songBase=song_id)[:20]
            results = [ob.song.as_json() for ob in objs]
            return HttpResponse(json.dumps(results), content_type="application/json")
        except Song.DoesNotExist:
            results = {}
            results['status'] = 404
            results['message'] = "Songs Not Found"
            return HttpResponseNotFound(HttpResponse(json.dumps(results), content_type="application/json"))
    else: # Qualquer coisa diferente de um GET eh probido e negado
        return HttpResponseForbidden()
