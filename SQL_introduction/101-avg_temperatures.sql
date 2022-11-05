-- displays average temperature (F) by city

SELECT city, AVG(value) AS average
FROM temperatures
GROUP BY city
ORDER BY average DESC;
