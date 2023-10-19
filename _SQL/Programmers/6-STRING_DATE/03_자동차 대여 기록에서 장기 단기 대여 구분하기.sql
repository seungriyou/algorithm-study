# https://school.programmers.co.kr/learn/courses/30/lessons/151138

SELECT
    history_id
    , car_id
    , DATE_FORMAT(start_date, '%Y-%m-%d')
    , DATE_FORMAT(end_date, '%Y-%m-%d')
    , IF(DATEDIFF(end_date, start_date) + 1 >= 30, '장기 대여', '단기 대여') AS rent_type
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(start_date, '%Y-%m') = '2022-09'
ORDER BY history_id DESC;
