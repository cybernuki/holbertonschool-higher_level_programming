-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT s.title FROM tv_shows s INNER JOIN tv_show_genres sg ON s.id = sg.show_id INNER JOIN tv_genres g ON sg.genre_id = g.id AND g.name = "Comedy"  ORDER BY s.title ASC;
