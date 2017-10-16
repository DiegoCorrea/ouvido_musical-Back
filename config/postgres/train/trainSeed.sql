\COPY songs_song FROM 'config/postgres/train/distinctSongTrain.seed' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/postgres/train/distinctUserTrain.seed' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'config/postgres/train/distinctPlayTrain.seed' DELIMITER ',' CSV HEADER;
