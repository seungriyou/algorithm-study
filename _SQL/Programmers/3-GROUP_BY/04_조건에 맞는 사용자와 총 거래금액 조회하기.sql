# https://school.programmers.co.kr/learn/courses/30/lessons/164668

SELECT U.user_id, U.nickname, SUM(B.price) AS total_sales
FROM USED_GOODS_BOARD B
INNER JOIN USED_GOODS_USER U ON B.writer_id = U.user_id
WHERE B.status = 'DONE'
GROUP BY B.writer_id
HAVING total_sales >= 700000
ORDER BY total_sales;
