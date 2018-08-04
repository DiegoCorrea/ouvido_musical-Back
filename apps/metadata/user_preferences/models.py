from django.db import models

from apps.metadata.users.models import User
from apps.metadata.songs.models import Song


class UserPreference(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, unique=False, related_name='song', on_delete=models.CASCADE)
    play_count = models.IntegerField(default=0, unique=False)

    class Meta:
        unique_together = (('user', 'song'),)

    def as_json(self):
        return dict(
            user_id=self.user_id,
            song_id=self.song_id,
            play_count=self.play_count,
        )
