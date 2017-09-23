from django.conf.urls import url

from api.songs import views as songView
from api.users import views as userView
from api.userPlaySong import views as userPlaySongView
from api.userSongRecommendation import views as userSongRecommendationView

urlpatterns = [
# Songs URL's
    url(r'^songs/$', songView.index, name='Index de Musicas'),
    url(r'^songs/allSongs$', songView.allSongs, name='Index de Musicas'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/$', songView.song, name='Uma Musica'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/similares$', songView.songSimilares, name='Musicas Similares'),
# Users URL's
    url(r'^users/$', userView.index, name='Index de Musicas'),
    url(r'^users/allUsers$', userView.allUsers, name='Index de Musicas'),
    url(r'^users/(?P<user_id>([a-zA-Z]|[0-9])+)/$',
        userView.user, name='O Usuarios'),
# Users Play Song URL's
    url(r'^users/(?P<user_id>([a-zA-Z]|[0-9])+)/songs/$',
        userPlaySongView.userSongs, name='As Musicas do Usuario'),
    url(r'^users/(?P<user_id>([a-zA-Z]|[0-9])+)/songs/(?P<song_id>([a-zA-Z]|[0-9])+)/$',
        userPlaySongView.userPlaySong, name='A Musica e o Usuario'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/hearby/$',
        userPlaySongView.songHearBy, name='A Musica ouvida por'),
    url(r'^songs/(?P<song_id>([a-zA-Z]|[0-9])+)/hearby/(?P<user_id>([a-zA-Z]|[0-9])+)$',
        userPlaySongView.songHearByUser, name='A Musica ouvida pelo usuario'),
    url(r'^songs/mostPlayedSongs$', userPlaySongView.mostPlayedSongsResource, name='Musicas mais tocadas'),
# User Song Recommendation URL's

]
