# https://school.programmers.co.kr/learn/courses/30/lessons/157340

SELECT
    car_id
    , IF(SUM(start_date <= '2022-10-16' AND end_date >= '2022-10-16') = 0, '대여 가능', '대여중') AS availability
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY car_id
ORDER BY car_id DESC;
