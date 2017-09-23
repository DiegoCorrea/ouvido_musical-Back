from django.db import models

from api.users.models import User
from api.songs.models import Song

# Create your models here.
class UserPlaySong(models.Model):
    user = models.ForeignKey(User, unique=False)
    song = models.ForeignKey(Song, unique=False)
    play_count = models.IntegerField(default=0, unique=False)

    def as_json(self):
        return dict(
            user_id=self.user_id,
            song_id=self.song_id,
            play_count=self.play_count,
        )
