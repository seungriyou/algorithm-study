# https://leetcode.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        # Write your MySQL query statement below.
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT N, 1  # -- LIMIT cannot recognize expressions w/ arithmetic operators! (math는 LIMIT 이전에...)
    );
END

# ===== (23.12.17) reviewed =====
# (1) LIMIT & OFFSET (NULL 자동)
BEGIN
  SET N = N - 1;
  RETURN (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET N
  );
END

# (2) window function
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT salary
      FROM (
        SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS _rank
        FROM Employee
      ) E
      WHERE _rank = N
  );
END
