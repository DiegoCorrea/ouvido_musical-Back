from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='UserIndex'),

    url(r'^all/$', views.users, name='Usuarios - Index'),
    url(r'^(?P<user_id>([a-zA-Z]|[0-9])+)/$',
        views.user, name='O Usuarios'),

    url(r'^(?P<user_id>([a-zA-Z]|[0-9])+)/songs/$',
        views.userSongs, name='As Musicas do Usuario'),
    url(r'^(?P<user_id>([a-zA-Z]|[0-9])+)/songs/(?P<song_id>([a-zA-Z]|[0-9])+)/$',
        views.userPlaySong, name='A Musica e o Usuario'),

    url(r'^(?P<user_id>([a-zA-Z]|[0-9])+)/recommendations/$',
        views.userSimilarity, name='Similaridade'),
    url(r'^(?P<user_id>([a-zA-Z]|[0-9])+)/recommendations/(?P<song_id>([a-zA-Z]|[0-9])+)/$',
        views.UserMusicRecommendation, name='User Musica Recommendation'),
    url(r'^(?P<user_id>([a-zA-Z]|[0-9])+)/recommendations/(?P<song_id>([a-zA-Z]|[0-9])+)/like/$',
        views.UserLikeMusicRecommendation, name='User Like Music'),
    #url(r'^users/(?P<user_id>([a-zA-Z]|[0-9])+)/similarity/with/(?P<user_id>([a-zA-Z]|[0-9])+)$',
    #   views.userSimilarityWith, name='Similaridade Entre Usuarios'),
]
