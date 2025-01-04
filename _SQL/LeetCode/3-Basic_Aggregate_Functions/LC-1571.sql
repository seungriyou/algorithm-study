-- https://leetcode.com/problems/warehouse-manager/

SELECT name as 'warehouse_name', SUM(units * width * length * height) as 'volume'
FROM warehouse w
INNER JOIN products p USING(product_id)
GROUP BY name;
