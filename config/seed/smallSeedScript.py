from api.songs.models import Song
from api.users.models import UserPlaySong
from api.users.models import User

def saveOnDBSong(line):
    song = Song()
    song.song = line[0]
    song.title = line[1].replace('"', '')
    song.album = line[2].replace('"', '')
    song.artist = line[3].replace('"', '')
    song.year = line[4]
    song.save()
    print(song.title + '\n')

for line in open('config/seed/smallSongEntry.seed', 'r'):
   line =  line.split(',')
   saveOnDBSong(line)

for line in open('config/seed/smallUserEntry.seed', 'r'):
   line =  line.split('\t')
   user = User()
   user.user = line[0]
   user.save()
   userPlaySong = UserPlaySong()
   userPlaySong.user_id = line[0]
   userPlaySong.song_id = line[1]
   userPlaySong.play_count = line[2]
   userPlaySong.save()
