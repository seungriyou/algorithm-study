# https://school.programmers.co.kr/learn/courses/30/lessons/132204

SELECT A.apnt_no, P.pt_name, A.pt_no, A.mcdp_cd, D.dr_name, A.apnt_ymd
FROM (
    SELECT apnt_no, pt_no, mcdp_cd, mddr_id, apnt_ymd
    FROM APPOINTMENT
    WHERE DATE_FORMAT(apnt_ymd, '%Y-%m-%d') = '2022-04-13' AND apnt_cncl_yn = 'N' AND mcdp_cd = 'CS'
) A
INNER JOIN PATIENT P ON A.pt_no = P.pt_no
INNER JOIN DOCTOR D ON A.mddr_id = D.dr_id
ORDER BY apnt_ymd;
