# https://leetcode.com/problems/students-and-examinations/

# MySQL은 FULL OUTER JOIN을 지원하지 X -> CROSS JOIN
# COALESCE() : parameter 중 NULL이 아닌 첫 원소 반환

# SELECT S.student_id, S.student_name, S.subject_name, IFNULL(E.cnt, 0) AS attended_exams
# FROM (SELECT * FROM Students, Subjects) AS S
# LEFT JOIN (
#     SELECT *, COUNT(*) AS cnt
#     FROM Examinations
#     GROUP BY student_id, subject_name
# ) AS E ON (E.student_id, E.subject_name) = (S.student_id, S.subject_name)
# ORDER BY S.student_id, S.subject_name;

SELECT S.student_id, S.student_name, Sub.subject_name, COALESCE(E.cnt, 0) AS attended_exams
FROM Students S
CROSS JOIN Subjects Sub
LEFT JOIN (
    SELECT *, COUNT(*) AS cnt
    FROM Examinations
    GROUP BY student_id, subject_name
) E ON E.student_id = S.student_id AND E.subject_name = Sub.subject_name
ORDER BY S.student_id, Sub.subject_name;


# ===== (23.12.10) reviewed =====
# [sol1] subquery
SELECT S.student_id, S.student_name, S.subject_name, COALESCE(E.cnt, 0) AS attended_exams
FROM (
    SELECT *
    FROM Students, Subjects
) S
LEFT JOIN (
    SELECT *, COUNT(*) AS cnt
    FROM Examinations
    GROUP BY student_id, subject_name
) E ON S.student_id = E.student_id AND S.subject_name = E.subject_name
ORDER BY 1, 3;

# [sol2] cross join
SELECT S1.student_id, S1.student_name, S2.subject_name, COALESCE(E.cnt, 0) AS attended_exams
FROM Students S1
CROSS JOIN Subjects S2
LEFT JOIN(
    SELECT *, COUNT(*) AS cnt
    FROM Examinations
    GROUP BY student_id, subject_name
) E ON S1.student_id = E.student_id AND S2.subject_name = E.subject_name
ORDER BY 1, 3;