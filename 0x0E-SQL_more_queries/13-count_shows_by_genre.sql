-- This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name, COUNT(g.name) AS number_of_shows FROM tv_shows s INNER JOIN tv_show_genres sg ON s.id = sg.show_id INNER JOIN tv_genres g ON g.id = sg.genre_id GROUP BY g.name ORDER BY number_of_shows DESC;
