# Write your MySQL query statement below
SELECT p.product_id as product_id, sum(s.quantity) as total_quantity
FROM Product p
JOIN Sales s
ON p.product_id = s.product_id
GROUP BY p.product_id