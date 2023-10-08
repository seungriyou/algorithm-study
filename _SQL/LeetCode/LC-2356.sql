# https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt    # -- COUNT() 안에도 DISTINCT를 쓸 수 있다!
FROM Teacher
GROUP BY teacher_id;
