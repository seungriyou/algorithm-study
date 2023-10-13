# https://school.programmers.co.kr/learn/courses/30/lessons/144854

SELECT B.book_id, A.author_name, DATE_FORMAT(B.published_date, '%Y-%m-%d') AS published_date
FROM BOOK B
INNER JOIN AUTHOR A ON B.author_id = A.author_id
WHERE category = '경제'
ORDER BY published_date;
