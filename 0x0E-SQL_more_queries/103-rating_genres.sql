-- This script lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(rate) rating 
FROM tv_show_ratings r 
    INNER JOIN tv_show_genres sg ON sg.show_id = r.show_id 
    INNER JOIN tv_genres g ON g.id = sg.genre_id 
GROUP BY sg.genre_id 
ORDER BY rating DESC;
