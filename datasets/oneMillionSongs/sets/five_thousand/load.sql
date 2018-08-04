\COPY songs_song FROM 'datasets/oneMillionSongs/sets/five_thousand/songs.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'datasets/oneMillionSongs/sets/five_thousand/users.csv' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'datasets/oneMillionSongs/sets/five_thousand/playCount.csv' DELIMITER ',' CSV HEADER;
