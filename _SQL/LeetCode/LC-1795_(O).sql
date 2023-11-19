# https://leetcode.com/problems/rearrange-products-table/

SELECT product_id, 'store1' AS store, store1 AS price   # -- UNION 시 first query에서 column name 결정하므로, 이후에는 alias 설정 안 해도 ok!
FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2', store2
FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3', store3
FROM Products
WHERE store3 IS NOT NULL;
