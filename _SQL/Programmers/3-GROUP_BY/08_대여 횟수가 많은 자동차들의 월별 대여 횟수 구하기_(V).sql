# https://school.programmers.co.kr/learn/courses/30/lessons/151139

SELECT
    MONTH(start_date) AS month
    , car_id
    , COUNT(*) AS records
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE car_id IN (
        SELECT car_id
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
        GROUP BY car_id
        HAVING COUNT(*) >= 5
    ) AND start_date BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY car_id, month
ORDER BY 1, 2 DESC;
