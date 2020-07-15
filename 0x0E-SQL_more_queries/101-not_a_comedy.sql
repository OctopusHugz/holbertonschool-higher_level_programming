-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT ts.title
FROM tv_shows AS ts,
	tv_genres AS tg
WHERE tg.name != "Comedy"
	AND ts.title NOT IN (
		SELECT ts.title
		FROM tv_shows AS ts
			LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
			LEFT JOIN tv_genres AS tg ON tsg.genre_id = tg.id
		WHERE tg.name = "Comedy"
	)
ORDER BY ts.title;
