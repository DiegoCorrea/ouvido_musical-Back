\COPY songs_song FROM 'config/data/oneMillionSongs/threeThousand/songs.csv' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/data/oneMillionSongs/threeThousand/users.csv' CSV HEADER;
\COPY "userPlaySong_userplaysong"(user_id,song_id,play_count) FROM 'config/data/oneMillionSongs/threeThousand/playCount.csv' DELIMITER ',' CSV HEADER;
