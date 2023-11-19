# https://leetcode.com/problems/the-latest-login-in-2020/

SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020   # -- '2020'으로 안 해도 되는구나...? ㅠㅋ
GROUP BY 1;
