-- displays the max temperature of each state (ordered by State name).
-- MAx() function
SELECT state, MAX(VALUE) as max_temp
FROM temperatures 
GROUP BY STATE 
ORDER BY 1;
