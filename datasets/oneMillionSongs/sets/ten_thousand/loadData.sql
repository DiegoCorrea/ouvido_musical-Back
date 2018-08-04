\COPY songs_song FROM 'config/data/oneMillionSongs/sets/ten_thousand/songs.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/data/oneMillionSongs/sets/ten_thousand/users.csv' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'config/data/oneMillionSongs/sets/ten_thousand/playCount.csv' DELIMITER ',' CSV HEADER;
