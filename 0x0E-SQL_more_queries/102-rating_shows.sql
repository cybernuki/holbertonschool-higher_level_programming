-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT s.title, SUM(rate) rating 
FROM tv_show_ratings r 
    INNER JOIN tv_shows s ON s.id = r.show_id 
GROUP BY show_id 
ORDER BY rating DESC;
