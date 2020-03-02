-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Order by avg temp
SELECT city, avg(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY 2 DESC;
