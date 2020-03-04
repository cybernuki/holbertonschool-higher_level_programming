-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT s.title FROM tv_shows s 
    LEFT JOIN tv_show_genres sg ON sg.show_id = s.id 
WHERE s.title NOT IN (
        SELECT s.title FROM tv_shows s 
        INNER JOIN tv_show_genres sg ON sg.show_id = s.id 
        INNER JOIN tv_genres g ON g.id = sg.genre_id AND g.name =  "Comedy"
        ) 
ORDER BY s.title;
