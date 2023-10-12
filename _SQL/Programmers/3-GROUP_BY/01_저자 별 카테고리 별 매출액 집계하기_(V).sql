# https://school.programmers.co.kr/learn/courses/30/lessons/144856

# SELECT A.author_id, A.author_name, B.category, SUM(B.price * BS.sales_cnt) AS total_sales
# FROM (
#     SELECT book_id, SUM(sales) AS sales_cnt
#     FROM BOOK_SALES
#     WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-01'
#     GROUP BY book_id
# ) AS BS
# LEFT JOIN BOOK B ON BS.book_id = B.book_id
# LEFT JOIN AUTHOR A ON A.author_id = B.author_id
# GROUP BY A.author_name, B.category
# ORDER BY 1, 3 DESC;

SELECT A.author_id, A.author_name, B.category, SUM(B.price * S.sales) AS total_sales
FROM BOOK_SALES S, BOOK B, AUTHOR A
WHERE
    S.book_id = B.book_id
    AND A.author_id = B.author_id
    AND DATE_FORMAT(sales_date, '%Y-%m') = '2022-01'
GROUP BY A.author_name, B.category
ORDER BY 1, 3 DESC;
