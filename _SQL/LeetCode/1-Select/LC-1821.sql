-- https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/

SELECT customer_id
FROM customers
WHERE year = '2021' and revenue > 0;
