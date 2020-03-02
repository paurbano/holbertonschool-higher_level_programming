--  displays the top 3 of cities temperature during July and August ordered by temperature (descending)
--  limit number of row selected
SELECT city, avg(value) as avg_temp 
FROM temperatures
WHERE (month = 7 OR month = 8)
GROUP BY city  
ORDER BY 2 DESC LIMIT 3;
