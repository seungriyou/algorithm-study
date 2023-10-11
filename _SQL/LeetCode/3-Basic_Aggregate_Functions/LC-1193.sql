# https://leetcode.com/problems/monthly-transactions-i/

SELECT
    # LEFT(trans_date, 7) AS month
    DATE_FORMAT(trans_date, '%Y-%m') AS month
    , country
    , COUNT(*) AS trans_count
    , SUM(IF(state = 'approved', 1, 0)) AS approved_count
    # , SUM(state = 'approved') AS approved_count
    , SUM(amount) AS trans_total_amount
    , SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
    # , SUM(
    #     CASE
    #     WHEN state = 'approved' THEN amount
    #     ELSE 0
    #     END
    # ) AS approved_total_amount
FROM Transactions
GROUP BY country, month
