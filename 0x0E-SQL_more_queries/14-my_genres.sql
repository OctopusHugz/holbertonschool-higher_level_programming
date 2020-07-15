-- This script uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tg.name
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
WHERE tsg.show_id = 8
ORDER BY tg.name ASC;
