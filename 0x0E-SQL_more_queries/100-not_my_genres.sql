--  list all genres not linked to the show Dexter
--  SUBQUERIES
SELECT DISTINCT tv_genres.name  AS name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows  ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name NOT IN (SELECT tv_genres.name
                            FROM tv_genres 
                            INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
                            INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
                            WHERE tv_shows.title = 'Dexter')
ORDER BY 1 ASC;
