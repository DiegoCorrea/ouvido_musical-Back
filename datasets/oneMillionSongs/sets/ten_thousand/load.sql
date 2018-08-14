\COPY songs_song FROM 'datasets/oneMillionSongs/sets/ten_thousand/songs.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'datasets/oneMillionSongs/sets/ten_thousand/users.csv' CSV HEADER;
\COPY "user_preferences_userpreference"(user_id,song_id,play_count) FROM 'datasets/oneMillionSongs/sets/ten_thousand/userCount.csv' DELIMITER ',' CSV HEADER;
