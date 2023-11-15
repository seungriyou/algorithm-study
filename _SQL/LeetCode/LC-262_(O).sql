# https://leetcode.com/problems/trips-and-users/

# cancellation rate = (# of canceled (by client or driver) requests with unbanned users) / (total # of requests with unbanned users) on that day

# 1. request_at between '2013-10-01' and '2013-10-03'
# 2. status <> 'completed'
# 3. client_id와 driver_id 모두 banned X

# ===== JOIN =====
SELECT
    T.request_at AS Day,
    ROUND(AVG(T.status != 'completed'), 2) AS 'Cancellation Rate'
FROM Trips T
INNER JOIN Users U1 ON T.client_id = U1.users_id
INNER JOIN Users U2 ON T.driver_id = U2.users_id
WHERE
    T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND U1.banned = 'No' AND U2.banned = 'No'
GROUP BY 1;


# ===== subquery =====
SELECT
    T.request_at AS Day,
    ROUND(AVG(T.status <> 'completed'), 2) AS 'Cancellation Rate'
FROM Trips T
WHERE
    T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND T.client_id IN (SELECT users_id FROM Users WHERE banned = 'No')
    AND T.driver_id IN (SELECT users_id FROM Users WHERE banned = 'No')
GROUP BY 1;
