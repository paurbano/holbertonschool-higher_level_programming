--  lists the number of records with the same score in the table second_table
--  group by clausule
SELECT score, COUNT(score) as number 
FROM second_table
GROUP by score
ORDER by 1 DESC;
