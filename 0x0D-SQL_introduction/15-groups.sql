-- This script lists the number of records with the same score in the table second_table
-- This query lists the number of records with the same score in the table second_table
SELECT score, COUNT(score) number FROM second_table GROUP BY score ORDER BY number DESC;
