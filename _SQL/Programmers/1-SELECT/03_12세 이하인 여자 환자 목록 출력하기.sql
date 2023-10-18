# https://school.programmers.co.kr/learn/courses/30/lessons/132201

SELECT pt_name, pt_no, gend_cd, age, COALESCE(tlno, 'NONE')
FROM PATIENT
WHERE age <= 12 AND gend_cd = 'W'
ORDER BY age DESC, pt_name;
