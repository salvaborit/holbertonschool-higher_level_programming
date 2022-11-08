-- lists all genres not linked to tv show 'Dexter'

-- SELECT sg.genre_id, g.name
-- FROM tv_shows s
--   JOIN tv_show_genres sg
--     ON s.id = sg.show_id
--   JOIN tv_genres g
--     ON g.id = sg.genre_id
-- WHERE s.title = 'Dexter'


SELECT *
  FROM tv_shows s



;
