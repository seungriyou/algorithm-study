# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

# SELECT V.customer_id, COUNT(V.visit_id) AS count_no_trans
# FROM Visits V
# WHERE V.visit_id NOT IN (
#     SELECT DISTINCT T.visit_id
#     FROM Transactions T
# )
# GROUP BY V.customer_id;

SELECT V.customer_id, COUNT(V.visit_id) AS count_no_trans
FROM Visits V
LEFT JOIN Transactions T ON V.visit_id = T.visit_id
WHERE T.visit_id is NULL
GROUP BY V.customer_id;
