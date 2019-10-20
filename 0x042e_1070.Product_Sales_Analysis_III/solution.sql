# Write your MySQL query statement below
SELECT s.product_id as product_id, f.first_year as first_year, quantity, price
FROM Sales s 
JOIN (
    SELECT product_id, MIN(year) as first_year
    FROM Sales
    GROUP BY product_id
) f
ON s.product_id = f.product_id AND s.year = f.first_year;