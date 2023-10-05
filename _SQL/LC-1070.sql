# https://leetcode.com/problems/product-sales-analysis-iii/

# === Subquery ===
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
);

# === JOIN ===
# SELECT S1.product_id, first_year, quantity, price
# FROM Sales S1
# INNER JOIN (
#     SELECT product_id, MIN(year) AS first_year
#     FROM Sales
#     GROUP BY product_id
# ) S2 ON S1.product_id = S2.product_id AND S1.year = S2.first_year;
