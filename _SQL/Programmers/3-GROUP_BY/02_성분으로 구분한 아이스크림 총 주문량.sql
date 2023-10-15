# https://school.programmers.co.kr/learn/courses/30/lessons/133026

SELECT ingredient_type, SUM(total_order) AS total_order
FROM ICECREAM_INFO I
INNER JOIN FIRST_HALF H ON I.flavor = H.flavor
GROUP BY ingredient_type
ORDER BY total_order;
