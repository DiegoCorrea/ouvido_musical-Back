\COPY songs_song FROM 'config/data/oneMillionSongs/fiveHundred/songs.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/data/oneMillionSongs/fiveHundred/users.csv' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'config/data/oneMillionSongs/fiveHundred/playCount.csv' DELIMITER ',' CSV HEADER;
