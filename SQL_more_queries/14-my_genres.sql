-- lists all genres of the tv show 'Dexter' on db 'hbtn_0d_tvshows'

SELECT g.name
FROM tv_genres g
RIght JOIN tv_show_genres sg
ON g.id = sg.genre_id
WHERE sg.show_id = 8;
