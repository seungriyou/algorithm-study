# https://school.programmers.co.kr/learn/courses/30/lessons/157339

SELECT
    C.car_id
    , C.car_type
    , ROUND(C.daily_fee * (1 - 0.01 * D.discount_rate) * (DATEDIFF('2022-11-30', '2022-11-01') + 1), 0) AS fee
FROM CAR_RENTAL_COMPANY_CAR C
INNER JOIN (
    SELECT car_type, CAST(duration_type AS UNSIGNED) AS duration_type, discount_rate
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE duration_type = DATEDIFF('2022-11-30', '2022-11-01') + 1
) AS D ON C.car_type = D.car_type
WHERE
    C.car_id NOT IN (
        SELECT car_id
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            DATE_FORMAT(start_date, '%Y-%m') = '2022-11'
            OR DATE_FORMAT(end_date, '%Y-%m') = '2022-11'
            OR (DATE_FORMAT(start_date, '%Y-%m') < '2022-11' AND DATE_FORMAT(end_date, '%Y-%m') > '2022-11')    # -- 2022-11 전부터 2022-11 후까지 대여하는 조건 까먹지 말기!!
    ) AND C.car_type IN ('SUV', '세단')
HAVING fee >= 500000 AND fee < 2000000
ORDER BY 3 DESC, 2, 1 DESC;

# ===== (23.11.24) REVIEWED =====
# car_type: '세단', 'SUV'
# 대여 기간: 2022-11-01 ~ 2022-11-30 30일간
# - end_date < 2022-11-01
# - start_date > 2022-11-30
# - start_date < 2022-11-01 AND end_date > 2022-11-30
# 30일간 대여 금액: 50만원 이상, 200만원 미만

SELECT C.car_id, C.car_type, TRUNCATE(30 * C.daily_fee * (1 - 0.01 * P.discount_rate), 0) AS fee
FROM CAR_RENTAL_COMPANY_CAR C
INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON C.car_type = P.car_type
WHERE
    C.car_type IN ('세단', 'SUV')
    AND C.car_id NOT IN (
        SELECT DISTINCT car_id
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            DATE_FORMAT(end_date, '%Y-%m') = '2022-11'
            OR DATE_FORMAT(start_date, '%Y-%m') = '2022-11'
            OR (DATE_FORMAT(start_date, '%Y-%m') < '2022-11' AND DATE_FORMAT(end_date, '%Y-%m') > '2022-11')
    )
    AND CAST(P.duration_type AS UNSIGNED) = 30
HAVING fee BETWEEN 500000 AND 2000000
ORDER BY 3 DESC, 2, 1 DESC;
