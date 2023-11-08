# https://school.programmers.co.kr/learn/courses/30/lessons/131535

SELECT COUNT(user_id) AS users
FROM USER_INFO
WHERE YEAR(joined) = '2021' AND age BETWEEN 20 AND 29;
