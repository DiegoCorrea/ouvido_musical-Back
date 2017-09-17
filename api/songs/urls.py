from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='SongIndex'),
    url(r'^songs/$', views.songs, name='Musicas Index'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/$', views.song, name='A Musica'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/hearby/$',
        views.songHearBy, name='A Musica ouvida por'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/hearby/(?P<user_id>([a-zA-Z]|[0-9])+)$',
        views.songHearByUser, name='A Musica ouvida pelo usuario'),
]
