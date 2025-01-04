-- https://leetcode.com/problems/sellers-with-no-sales/

-- subquery
SELECT seller_name
FROM Seller
WHERE seller_id NOT IN (
    SELECT DISTINCT seller_id
    FROM Orders
    WHERE YEAR(sale_date) = '2020'
)
ORDER BY 1;

-- left join
SELECT seller_name
FROM Seller S
LEFT JOIN Orders O ON (
    S.seller_id = O.seller_id AND YEAR(O.sale_date) = "2020"
)
WHERE O.order_id IS NULL
ORDER BY 1;

-- having
SELECT seller_name
FROM Seller S
LEFT JOIN Orders O USING(seller_id)
GROUP BY S.seller_id
HAVING SUM(IFNULL(YEAR(sale_date) = "2020", 0)) = 0
ORDER BY 1;
