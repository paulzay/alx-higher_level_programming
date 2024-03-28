-- no genre
SELECT tv_shows.title, tv_show_genres.genre_id
        FROM tv_shows_genres
        FULL JOIN tv_shows
        ON tv_shows.genre_id IS NULL
        ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
