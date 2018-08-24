\COPY songs_song FROM 'datasets/oneMillionSongs/sets/25000/songs.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'datasets/oneMillionSongs/sets/25000/users.csv' CSV HEADER;
\COPY "user_preferences_userpreference"(user_id,song_id,play_count) FROM 'datasets/oneMillionSongs/sets/25000/playCount.csv' DELIMITER ',' CSV HEADER;
