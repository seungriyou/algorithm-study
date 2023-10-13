# https://school.programmers.co.kr/learn/courses/30/lessons/131114

SELECT warehouse_id, warehouse_name, address, IFNULL(freezer_yn, 'N')
FROM FOOD_WAREHOUSE
WHERE address LIKE '경기도%';
