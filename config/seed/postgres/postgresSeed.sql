\COPY songs_song FROM 'config/seed/postgres/smallSongEntry.seed' DELIMITER ',' CSV HEADER;
\COPY users_user FROM 'config/seed/postgres/smallUserEntry.seed' CSV HEADER;
\COPY users_userplaysong FROM 'config/seed/postgres/smallUserPlaySongEntry.seed' DELIMITER ',' CSV HEADER;
