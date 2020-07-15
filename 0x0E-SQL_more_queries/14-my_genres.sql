-- This script uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
/* SELECT tsg.genre_id name
FROM tv_show_genres AS tsg
	INNER JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE tsg.show_id = 8; */
/* ORDER BY name ASC; */
/* SELECT tsg.genre_id name
FROM tv_show_genres AS tsg
WHERE tsg.show_id = 8; */
SELECT tg.name
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
WHERE tsg.show_id = 8
ORDER BY tg.name ASC;
