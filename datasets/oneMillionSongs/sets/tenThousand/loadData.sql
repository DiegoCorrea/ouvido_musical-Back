\COPY songs_song FROM 'config/data/oneMillionSongs/tenThousand/songs.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/data/oneMillionSongs/tenThousand/users.csv' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'config/data/oneMillionSongs/tenThousand/playCount.csv' DELIMITER ',' CSV HEADER;
