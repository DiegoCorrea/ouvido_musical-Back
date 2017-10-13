\COPY songs_song FROM 'config/postgres/bigger/songEntry.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/postgres/bigger/userEntry.csv' CSV HEADER;
\COPY "userPlaySong_userplaysong"(id,user_id,song_id,play_count) FROM 'config/postgres/bigger/smallUserPlaySongEntry.csv' DELIMITER '\t' CSV HEADER;
