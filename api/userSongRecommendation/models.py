from django.db import models

from api.users.models import User
from api.songs.models import Song

# Create your models here.
class UserSongRecommendation(models.Model):
    user = models.ForeignKey(User, unique=False)
    song = models.ForeignKey(Song, unique=False)
    probabilit_play_count = models.IntegerField(default=0, unique=False)
    iLike = models.BooleanField(default=False)

    def as_json(self):
        return dict(
            song_id=self.song_id,
            user_id=self.user_id,
            probabilit_play_count=self.probabilit_play_count,
            iLike=self.iLike
        )
