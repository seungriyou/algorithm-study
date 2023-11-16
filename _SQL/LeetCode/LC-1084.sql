# https://leetcode.com/problems/sales-analysis-iii/

# ===== subquery =====
SELECT DISTINCT product_id, product_name    # -- DISTINCT를 잊지말자.....
FROM Sales S
INNER JOIN Product P USING(product_id)
WHERE product_id NOT IN (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE NOT (sale_date BETWEEN '2019-01-01' AND '2019-03-31')
);

# ===== group by =====
SELECT product_id, product_name
FROM Sales S
INNER JOIN Product P USING(product_id)
GROUP BY product_id
HAVING SUM(sale_date < '2019-01-01' OR sale_date > '2019-03-31') = 0;
