# https://school.programmers.co.kr/learn/courses/30/lessons/293259
# subquery가 반드시 필요하지 않은 경우가 있다!
SELECT ROUND(AVG(COALESCE(length, 10)), 2) AS average_length
FROM FISH_INFO;
