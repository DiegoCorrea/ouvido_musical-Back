from django.http import HttpResponse, JsonResponse

from apps.metadata.users.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def user(request, userid=''):
    if request.method == 'GET':
        return show(userid)
    elif request.method == 'POST':
        return edit(userid)
    elif request.method == 'DELETE':
        return remove(userid)
    return HttpResponse("User_ID: Falhou a obter as informações!")


def remove(id):
    return HttpResponse("DELETE User_ID")


def show(id):
    try:
        user = User.objects.get(id=id)
        return JsonResponse(status=200, data={'id': str(user.id)})
    except Exception as e:
        return HttpResponse(str(e))


def edit(id):
    return HttpResponse("EDIT User_ID")
