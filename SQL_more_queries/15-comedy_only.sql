-- lists all 'Comedy' tv shows in db 'hbtn_0d_tvshows'

SELECT s.title
FROM tv_shows s
JOIN tv_show_genres sg
ON s.id = sg.show_id
WHERE sg.genre_id = 5
ORDER BY s.title;
