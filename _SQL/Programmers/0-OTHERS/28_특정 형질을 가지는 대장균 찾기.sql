# https://school.programmers.co.kr/learn/courses/30/lessons/301646
SELECT COUNT(id) AS count
FROM ECOLI_DATA
WHERE !(genotype & 2) AND genotype & 5;
