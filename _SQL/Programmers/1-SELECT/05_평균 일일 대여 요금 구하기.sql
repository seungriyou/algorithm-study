# https://school.programmers.co.kr/learn/courses/30/lessons/151136

SELECT ROUND(AVG(daily_fee), 0) AS average_fee
FROM CAR_RENTAL_COMPANY_CAR
WHERE car_type = 'SUV';
