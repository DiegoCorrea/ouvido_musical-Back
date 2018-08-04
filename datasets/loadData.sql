\COPY songs_song FROM 'config/postgres/dez/songs.seed' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/postgres/dez/users.seed' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'config/postgres/dez/userPlaySong.seed' DELIMITER ',' CSV HEADER;
