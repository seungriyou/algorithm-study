# https://school.programmers.co.kr/learn/courses/30/lessons/151141

SELECT
    H.history_id
    , ROUND(
        C.daily_fee * (1 - 0.01 * COALESCE(MAX(D.discount_rate), 0)) * (DATEDIFF(H.end_date, H.start_date) + 1)
    ) AS fee    # -- MAX(D.discount_rate): 대여일수가 많을수록 discount_rate이 클 것이므로...!
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
INNER JOIN CAR_RENTAL_COMPANY_CAR C
    ON H.car_id = C.car_id
    AND C.car_type = '트럭'
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
    ON C.car_type = D.car_type
    AND DATEDIFF(H.end_date, H.start_date) + 1 >= CAST(D.duration_type AS UNSIGNED)
GROUP BY history_id
ORDER BY 2 DESC, 1 DESC;
