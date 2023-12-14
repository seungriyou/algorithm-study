# https://leetcode.com/problems/investments-in-2016/

# === w/o partition by ===
# SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
# FROM Insurance
# WHERE tiv_2015 IN (
#     SELECT tiv_2015
#     FROM Insurance
#     GROUP BY tiv_2015
#     HAVING COUNT(*) > 1
# ) AND (lat, lon) IN (
#     SELECT lat, lon
#     FROM Insurance
#     GROUP BY lat, lon
#     HAVING COUNT(*) = 1
# );

# === w/ parition by ===
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT
        tiv_2016
        , COUNT(*) OVER(PARTITION BY tiv_2015) AS cnt1
        , COUNT(*) OVER(PARTITION BY lat, lon) AS cnt2
    FROM Insurance
) AS T
WHERE cnt1 > 1 AND cnt2 = 1;

# ===== (23.12.14) reviewed =====
# ----- w/o window function -----
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE
    tiv_2015 IN (
        SELECT tiv_2015
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(pid) > 1   # t_cnt > 1이어야 함
    ) AND
    (lat, lon) IN (
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(pid) = 1   # l_cnt = 1이어야 함
    );

# ----- w/ window function -----
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS t_cnt,
        COUNT(*) OVER (PARTITION BY lat, lon) AS l_cnt
    FROM Insurance
) I
WHERE t_cnt > 1 AND l_cnt = 1;
