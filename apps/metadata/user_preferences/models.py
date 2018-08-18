from django.db import models

from apps.metadata.songs.models import Song
from apps.metadata.users.models import User


class UserPreference(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, unique=False, related_name='song', on_delete=models.CASCADE)
    play_count = models.IntegerField(default=0, unique=False)

    class Meta:
        unique_together = (('user', 'song'),)
