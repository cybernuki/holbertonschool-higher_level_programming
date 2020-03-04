-- This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name FROM tv_genres WHERE name NOT IN (SELECT g.name FROM tv_shows s INNER JOIN tv_show_genres sg ON s.id = sg.show_id AND s.title = "Dexter" INNER JOIN tv_genres g ON sg.genre_id = g.id  ORDER BY g.name ASC) ORDER BY name;
