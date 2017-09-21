# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.http import JsonResponse

from .models import User

# Create your views here.
def index(request):
    return JsonResponse({'status': 200, 'message': 'Home'})

def allUsers(request):
    results = {}
    try:
        results = [ob.as_json() for ob in User.objects.all().order_by('id')[:20]]
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
