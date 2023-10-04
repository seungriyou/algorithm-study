# https://leetcode.com/problems/confirmation-rate/

# SELECT S.user_id, IFNULL(C.rate, 0) AS confirmation_rate
# FROM Signups S
# LEFT JOIN (
#     SELECT user_id, ROUND(AVG(IF(action = 'confirmed', 1, 0)), 2) AS rate
#     FROM Confirmations
#     GROUP BY user_id
# ) AS C USING (user_id);

SELECT S.user_id, ROUND(AVG(IF(action = 'confirmed', 1, 0)), 2) AS confirmation_rate
FROM Signups S
LEFT JOIN Confirmations C USING (user_id)
GROUP BY user_id;
