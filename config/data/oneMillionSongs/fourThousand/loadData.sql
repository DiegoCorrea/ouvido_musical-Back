\COPY songs_song FROM 'config/data/oneMillionSongs/fourThousand/songs.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/data/oneMillionSongs/fourThousand/users.csv' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'config/data/oneMillionSongs/fourThousand/playCount.csv' DELIMITER ',' CSV HEADER;
