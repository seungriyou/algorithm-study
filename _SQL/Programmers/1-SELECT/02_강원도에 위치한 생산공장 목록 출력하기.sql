# https://school.programmers.co.kr/learn/courses/30/lessons/131112

SELECT factory_id, factory_name, address
FROM FOOD_FACTORY
# WHERE LEFT(address, 3) = '강원도'
WHERE address LIKE '강원도%'
ORDER BY factory_id;
