-- cities of California that can be found in the database hbtn_0d_usa.
-- OLD FORM JOIN
SELECT cities.id, cities.name 
FROM cities , states 
WHERE cities.state_id=states.id AND 
    states.name='California '
ORDER BY cities.id;
