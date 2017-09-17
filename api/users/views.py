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

def index(request, user_id):
    print("User Index")
