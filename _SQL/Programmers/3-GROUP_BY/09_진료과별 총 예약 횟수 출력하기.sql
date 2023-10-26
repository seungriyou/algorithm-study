# https://school.programmers.co.kr/learn/courses/30/lessons/132202
SELECT mcdp_cd AS '진료과 코드', COUNT(pt_no) AS '5월 예약건수'
FROM APPOINTMENT
WHERE YEAR(apnt_ymd) = '2022' AND MONTH(apnt_ymd) = '05'
GROUP BY mcdp_cd
ORDER BY 2, 1;
