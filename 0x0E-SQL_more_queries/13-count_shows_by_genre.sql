-- This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
/* SELECT tg.name genre, COUNT(tsg.show_id) AS number_of_shows
 FROM tv_genres as tg, tv_show_genres as tsg
 GROUP BY tg.name
 ORDER BY number_of_shows DESC; */
/* SELECT tg.name genre,
 COUNT(tsg.genre_id = tg.id) AS number_of_shows
 FROM tv_genres as tg,
 tv_show_genres as tsg
 GROUP BY tg.name
 ORDER BY number_of_shows DESC; */
/* SELECT tsg.show_id genre,
 COUNT(*) as number_of_shows
 FROM tv_show_genres as tsg
 GROUP BY tsg.show_id
 ORDER BY number_of_shows DESC; */
/* SELECT tg.name genre,
 COUNT(*) as number_of_shows
 FROM tv_genres as tg
 GROUP BY tg.name
 ORDER BY number_of_shows DESC; */
/* SELECT tg.name genre,
 tsg.show_id
 FROM tv_genres AS tg
 LEFT JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id */
/* SELECT tg.name genre
 FROM tv_genres AS tg; */
SELECT tg.name genre,
	COUNT(*) AS number_of_shows
FROM tv_genres AS tg
	LEFT JOIN tv_show_genres as tsg ON tg.id = tsg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
