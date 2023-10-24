# https://school.programmers.co.kr/learn/courses/30/lessons/131120

SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth, '%Y-%m-%d') AS date_of_birth
FROM MEMBER_PROFILE
WHERE MONTH(date_of_birth) = '03' AND tlno IS NOT NULL AND gender = 'W'
ORDER BY member_id;
