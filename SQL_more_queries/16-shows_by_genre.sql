-- lists shows, genres linked to show
-- from db 'hbtn_0d_tvshows'

SELECT DISTINCT s.title, g.name
FROM tv_shows s, tv_genres g, tv_show_genres sg
WHERE (sg.show_id = s.id AND sg.genre_id = g.id)
ORDER BY s.title, g.name;
