\COPY songs_song FROM 'config/postgres/bigger/distinctSong.seed' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/postgres/bigger/distinctUser.seed' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'config/postgres/bigger/distinctPlay.seed' DELIMITER ',' CSV HEADER;
