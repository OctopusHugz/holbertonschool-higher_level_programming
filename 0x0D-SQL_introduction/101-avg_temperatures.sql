-- This script displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- This query displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) avg_temp GROUP BY city ORDER BY avg_temp DESC;
