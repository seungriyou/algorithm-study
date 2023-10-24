# https://school.programmers.co.kr/learn/courses/30/lessons/151137

SELECT car_type, COUNT(car_id) AS cars
FROM CAR_RENTAL_COMPANY_CAR
WHERE options REGEXP '통풍시트|열선시트|가죽시트'
# WHERE options LIKE '%통풍시트%' OR options LIKE '%열선시트%' OR options LIKE '%가죽시트%'
GROUP BY car_type
ORDER BY car_type;
