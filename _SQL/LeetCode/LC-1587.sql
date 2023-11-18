# https://leetcode.com/problems/bank-account-summary-ii/
SELECT name, SUM(amount) AS balance
FROM Users
INNER JOIN Transactions USING(account)
GROUP BY account
HAVING balance > 10000;
-- 굳이 subquery로 분리할 필요 없이 join 해서 group
