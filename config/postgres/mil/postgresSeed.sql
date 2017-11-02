\COPY songs_song FROM 'config/postgres/cemMil/distinctSong.seed' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/postgres/cemMil/distinctUser.seed' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'config/postgres/cemMil/distinctPlay.seed' DELIMITER ',' CSV HEADER;
