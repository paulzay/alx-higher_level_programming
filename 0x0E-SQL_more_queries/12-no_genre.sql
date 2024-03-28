-- no genre
SELECT tv_shows.title, tv_show_genres.genre_id
        FROM tv_shows_genres
        RIGHT JOIN tv_shows
        ON tv_shows.id = tv_show_genres.show_id
        WHERE tv_show_genres IS NULL
        ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
