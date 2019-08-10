# Write your MySQL query statement below
SELECT customer_id 
FROM
(
    SELECT customer_id, COUNT(DISTINCT(product_key)) as c1
    FROM Customer
    GROUP BY customer_id
) t1
JOIN
(
    SELECT COUNT(DISTINCT(product_key)) as c2
    FROM Product
) t2
ON t1.c1 = t2.c2;