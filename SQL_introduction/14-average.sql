-- computes the score average of all records
SELECT AVG(score), name
FROM second_table
GROUP BY name