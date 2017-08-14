from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Ouvido Musical Index'),

    url(r'^songs/$', views.songs, name='Musicas Index'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/$', views.song, name='A Musica'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/hearby/$', views.songHearBy, name='A Musica ouvida por'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/hearby/(?P<user_id>([a-zA-Z]|[0-9])+)$', views.songHearByUser, name='A Musica ouvida pelo usuario'),

    url(r'^users/$', views.users, name='Usuarios - Index'),
    url(r'^users/(?P<user_id>([a-zA-Z]|[0-9])+)/$', views.user, name='O Usuarios'),

    url(r'^users/(?P<user_id>([a-zA-Z]|[0-9])+)/songs/$', views.userSongs, name='As Musicas do Usuario'),
    url(r'^users/(?P<user_id>([a-zA-Z]|[0-9])+)/songs/(?P<song_id>([a-zA-Z]|[0-9])+)/$', views.userPlaySong, name='A Musica e o Usuario'),

    url(r'^users/(?P<user_id>([a-zA-Z]|[0-9])+)/recommendations/$', views.userSimilarity, name='Similaridade'),
    #url(r'^users/(?P<user_id>([a-zA-Z]|[0-9])+)/similarity/with/(?P<user_id>([a-zA-Z]|[0-9])+)$', views.userSimilarityWith, name='Similaridade Entre Usuarios'),

]
