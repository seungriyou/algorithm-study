# https://leetcode.com/problems/list-the-products-ordered-in-a-period/

SELECT P.product_name, O.sum_unit AS unit
FROM (
    SELECT product_id, SUM(unit) AS sum_unit
    FROM Orders
    WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY product_id
    HAVING sum_unit >= 100
) AS O
INNER JOIN Products P ON O.product_id = P.product_id;

# SELECT P.product_name, SUM(O.unit) AS unit
# FROM Products P
# INNER JOIN Orders O USING (product_id)
# WHERE YEAR(O.order_date) = '2020' AND MONTH(O.order_date) = '02'
# GROUP BY P.product_id
# HAVING unit >= 100;

# ===== (23.12.09) reviewed =====
SELECT product_name, SUM(unit) AS unit
FROM Orders
INNER JOIN Products USING(product_id)
WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'
GROUP BY product_id
HAVING unit >= 100; # MySQL에서 HAVING 절은 SELECT 절이나 outer subqueries에 있는 columns도 참조 가능
