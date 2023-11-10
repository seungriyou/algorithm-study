# https://school.programmers.co.kr/learn/courses/30/lessons/131528

SELECT COUNT(user_id) AS users
FROM USER_INFO
WHERE age IS NULL;
