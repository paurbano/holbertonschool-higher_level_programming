-- lists all shows contained
-- OUTER JOINS show doesn’t have a genre, display NULL
SELECT tv_shows.title,tv_show_genres.genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY 1,2;
