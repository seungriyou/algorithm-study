# https://leetcode.com/problems/group-sold-products-by-the-date/

SELECT
    sell_date
    , COUNT(DISTINCT product) AS num_sold
    , GROUP_CONCAT(DISTINCT product SEPARATOR '&') AS products    # -- ORDER BY product 할 필요 없음
FROM Activities
GROUP BY sell_date
ORDER BY sell_date, product;

# ===== (23.12.08) reviewed =====
SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    # GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
    GROUP_CONCAT(DISTINCT product ORDER BY product) AS products     # default separator = ','
FROM Activities
GROUP BY sell_date
ORDER BY 1;
