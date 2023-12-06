# https://leetcode.com/problems/average-time-of-process-per-machine/

SELECT A.machine_id, ROUND(AVG(B.timestamp - A.timestamp), 3) AS processing_time
FROM Activity A
INNER JOIN Activity B ON (A.machine_id, A.process_id) = (B.machine_id, B.process_id) AND B.activity_type = 'end'
WHERE A.activity_type = 'start'
GROUP BY A.machine_id;

# SELECT A.machine_id, ROUND(
#     (SELECT AVG(B.timestamp) FROM Activity B WHERE B.activity_type = 'end' AND B.machine_id = A.machine_id)
#     - (SELECT AVG(B.timestamp) FROM Activity B WHERE B.activity_type = 'start' AND B.machine_id = A.machine_id)
# , 3) AS processing_time
# FROM Activity A
# GROUP BY A.machine_id;

# ===== (23.12.06) reviewed =====
SELECT E.machine_id, ROUND(AVG(E.timestamp - S.timestamp), 3) AS processing_time
FROM Activity E
INNER JOIN Activity S
    ON (E.machine_id, E.process_id) = (S.machine_id, S.process_id)
    AND E.activity_type = 'end' AND S.activity_type = 'start'
GROUP BY 1;
