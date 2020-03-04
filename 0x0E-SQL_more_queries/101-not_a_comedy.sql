-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT s.title FROM tv_show_genres sg INNER JOIN tv_genres g ON g.id = sg.genre_id and g.name != "Comedy" INNER JOIN tv_shows s ON s.id = sg.show_id;
