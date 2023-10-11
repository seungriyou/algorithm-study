# https://leetcode.com/problems/count-salary-categories/

# SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count
# FROM Accounts
# WHERE income < 20000
# UNION
# SELECT 'Average Salary' AS category, COUNT(*) AS accounts_count
# FROM Accounts
# WHERE income BETWEEN 20000 AND 50000
# UNION
# SELECT 'High Salary' AS category, COUNT(*) AS accounts_count
# FROM Accounts
# WHERE income > 50000;

SELECT 'Low Salary' AS category, SUM(income < 20000) AS accounts_count
FROM Accounts
UNION
SELECT 'Average Salary' AS category, SUM(income BETWEEN 20000 AND 50000) AS accounts_count
FROM Accounts
UNION
SELECT 'High Salary' AS category, SUM(income > 50000) AS accounts_count
FROM Accounts;
