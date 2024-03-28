-- no genre
SELECT tv_shows.title, tv_show_genres.genre_id
        FROM tv_shows_genres
        RIGHT JOIN tv_shows
        WHERE show.id = tv_show_genres.show_id
        ON tv_shows.genre_id IS NULL
        ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
