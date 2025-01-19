-- https://leetcode.com/problems/apples-oranges/

-- join
SELECT a.sale_date, a.sold_num - b.sold_num AS diff
FROM Sales a
INNER JOIN Sales b ON a.sale_date = b.sale_date AND a.fruit = 'apples' AND b.fruit = 'oranges'
ORDER BY 1;

-- subquery & join
SELECT a.sale_date, a.sold_num - b.sold_num AS diff
FROM (SELECT * FROM Sales WHERE fruit = 'apples') a
INNER JOIN (SELECT * FROM Sales WHERE fruit = 'oranges') b USING(sale_date)
ORDER BY 1;

-- aggregation func & case
SELECT
    sale_date,
    SUM(
        CASE
            WHEN fruit = 'apples' THEN sold_num
            WHEN fruit = 'oranges' THEN -sold_num
        END
    ) AS diff
FROM Sales
GROUP BY 1
ORDER BY 1;
