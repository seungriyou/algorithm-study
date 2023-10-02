# https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN SUBDATE('2019-07-27', 29) AND '2019-07-27'
GROUP BY activity_date;
# HAVING activity_date BETWEEN SUBDATE('2019-07-27', 29) AND '2019-07-27';  # -- where 절에서 조건을 걸어줘야 group by 할 때 시간 덜 걸림
