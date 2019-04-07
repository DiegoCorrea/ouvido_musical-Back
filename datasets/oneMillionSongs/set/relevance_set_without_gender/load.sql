\COPY songs_song FROM 'datasets/oneMillionSongs/set/relevance_set/songs.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'datasets/oneMillionSongs/set/relevance_set/users.csv' CSV HEADER;\COPY
"user_preferences_userpreference"(user_id, song_id, play_count)FROM
'datasets/oneMillionSongs/set/relevance_set/preferences.csv' DELIMITER ',' CSV HEADER;
