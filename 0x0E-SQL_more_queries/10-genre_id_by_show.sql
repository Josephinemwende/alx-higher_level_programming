-- script that lists alls hows contaiend in a database --
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres ON show.id = genre.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
