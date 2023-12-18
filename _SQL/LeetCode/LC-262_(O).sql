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


# ===== (23.12.18) reviewed =====
# cancellation rate per day = canceled(by client / driver) requests with unbanned users / total number of requests with unbanned users
# unbanned users = both client & driver must not be banned
# 2013-10-01 ~ 2013-10-03

# (1) subquery
SELECT
    request_at AS Day,
    ROUND(AVG(status LIKE 'cancelled%'), 2) AS 'Cancellation Rate'  # SUM() / COUNT() 보다 AVG()가 더 빠르다
    # ROUND(AVG(status <> 'completed'), 2) AS 'Cancellation Rate'
FROM Trips
WHERE client_id IN (
    SELECT users_id
    FROM Users
    WHERE banned = 'No' AND role = 'client'
) AND driver_id IN (
    SELECT users_id
    FROM Users
    WHERE banned = 'No' AND role = 'driver'
) AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 1;

# (2) join
SELECT
    T.request_at AS Day,
    # ROUND(AVG(T.status LIKE 'cancelled%'), 2) AS 'Cancellation Rate'  # SUM() / COUNT() 보다 AVG()가 더 빠르다
    ROUND(AVG(T.status <> 'completed'), 2) AS 'Cancellation Rate'
FROM Trips T
INNER JOIN Users C ON T.client_id = C.users_id
INNER JOIN Users D ON T.driver_id = D.users_id
WHERE
    request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND C.banned = 'No' AND D.banned='No'
GROUP BY 1;
