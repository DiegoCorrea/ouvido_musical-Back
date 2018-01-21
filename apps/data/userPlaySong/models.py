from django.db import models

from apps.data.users.models import User
from apps.data.songs.models import Song


class UserPlaySong(models.Model):
    user = models.ForeignKey(User, unique=False)
    song = models.ForeignKey(Song, unique=False, related_name='song')
    play_count = models.IntegerField(default=0, unique=False)

    class Meta:
        unique_together = (('user', 'song'),)

    def as_json(self):
        return dict(
            user_id=self.user_id,
            song_id=self.song_id,
            play_count=self.play_count,
        )
