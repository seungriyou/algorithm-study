# https://school.programmers.co.kr/learn/courses/30/lessons/132203

SELECT dr_name, dr_id, mcdp_cd, DATE_FORMAT(hire_ymd, '%Y-%m-%d')
FROM DOCTOR
WHERE mcdp_cd IN ('CS', 'GS')
ORDER BY hire_ymd DESC, dr_name;
