from recommendations.models import Song
from recommendations.models import UserPlaySong
from recommendations.models import User

for line in open('scripts/seed/bigSongEntry.seed', 'r'):
   line =  line.split(',')
   song = Song()
   song.song = line[0]
   song.title = line[1].split('"')[1::2]
   song.album = line[2].split('"')[1::2]
   song.artist = line[3].split('"')[1::2]
   song.year = line[4]
   song.save()

for line in open('scripts/seed/bigUserEntry.seed', 'r'):
   line =  line.split('\t')
   user = User()
   user.user = line[0]
   user.save()
   userPlaySong = UserPlaySong()
   userPlaySong.user_id = line[0]
   userPlaySong.song_id = line[1]
   userPlaySong.play_count = line[2]
   userPlaySong.save()
