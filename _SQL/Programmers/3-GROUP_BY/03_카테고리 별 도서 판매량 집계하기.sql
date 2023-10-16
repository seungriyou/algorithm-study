# https://school.programmers.co.kr/learn/courses/30/lessons/144855

SELECT B.category, SUM(S.sales) AS TOTAL_SALES
FROM BOOK B
INNER JOIN BOOK_SALES S USING(book_id)
WHERE DATE_FORMAT(S.sales_date, '%Y-%m') = '2022-01'
GROUP BY B.category
ORDER BY B.category;
