# https://school.programmers.co.kr/learn/courses/30/lessons/157341

SELECT DISTINCT C.car_id
FROM CAR_RENTAL_COMPANY_CAR C
INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY R ON C.car_id = R.car_id
WHERE C.car_type = '세단' AND MONTH(R.start_date) = 10
ORDER BY C.car_id DESC;
