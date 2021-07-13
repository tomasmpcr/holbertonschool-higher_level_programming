-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name genre, COUNT(tv_genres.id) number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id GROUP BY tv_genres.id ORDER BY COUNT(tv_genres.id) DESC;
