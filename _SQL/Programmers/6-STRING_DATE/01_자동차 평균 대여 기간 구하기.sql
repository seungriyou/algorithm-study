# https://school.programmers.co.kr/learn/courses/30/lessons/157342

SELECT car_id, ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS average_duration
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY car_id
HAVING average_duration >= 7
ORDER BY 2 DESC, 1 DESC;
