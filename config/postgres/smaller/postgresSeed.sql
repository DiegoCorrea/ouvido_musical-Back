\COPY songs_song FROM 'config/postgres/smaller/smallSongEntry.seed' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/postgres/smaller/smallUserEntry.seed' CSV HEADER;
\COPY "userPlaySong_userplaysong"(id,user_id,song_id,play_count) FROM 'config/postgres/smaller/smallUserPlaySongEntry.seed' DELIMITER ',' CSV HEADER;
