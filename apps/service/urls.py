"""ouvidoMusical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from apps.service.songs import views as songs_views
from apps.service.users import views as users_views

urlpatterns = [
    url(r'^users/$', users_views.index),
    url(r'^users/(?P<user_id>\w+)/$', users_views.process_request, name='user'),
    url(r'^users/(?P<user_id>\w+)/recommendations/$', users_views.index_recommendations_request,
        name='user_recommendations'),
    url(r'^users/(?P<user_id>\w+)/songs/$', users_views.index_song_request, name='user_songs'),
    url(r'^users/(?P<user_id>\w+)/songs/(?P<song_id>\w+)$', users_views.song_request, name='user_songs'),
    url(r'^songs/$', songs_views.index, name='songs'),
    url(r'^songs/(?P<song_id>\w+)/$', songs_views.process_request, name='song'),
]
