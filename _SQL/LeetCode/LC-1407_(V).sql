# https://leetcode.com/problems/top-travellers/
SELECT U.name, COALESCE(SUM(R.distance), 0) AS travelled_distance
FROM Users U
LEFT JOIN RIDES R ON U.id = R.user_id
GROUP BY U.id   # 주의! (Users에는 있는 id지만 Rides에 없는 user_id도 고려하려면 R.user_id가 아닌 U.id로 group by)
ORDER BY 2 DESC, 1;
