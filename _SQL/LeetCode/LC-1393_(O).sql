# https://leetcode.com/problems/capital-gainloss/
# ===== w/o window function =====
SELECT
    stock_name,
    SUM(IF(operation = "Sell", price, -price)) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;

# ===== window function =====
SELECT stock_name, SUM(price - prev_price) AS capital_gain_loss
FROM (
    SELECT *, LAG(price) OVER (PARTITION BY stock_name ORDER BY operation_day) AS prev_price
    FROM Stocks
) S
WHERE operation = 'Sell'
GROUP BY stock_name;
