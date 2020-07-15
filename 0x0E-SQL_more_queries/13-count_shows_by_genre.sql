-- This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tg.name genre,
	COUNT(*) AS number_of_shows
FROM tv_genres AS tg
	LEFT JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
GROUP BY tg.id
ORDER BY number_of_shows DESC, tg.id ASC;
