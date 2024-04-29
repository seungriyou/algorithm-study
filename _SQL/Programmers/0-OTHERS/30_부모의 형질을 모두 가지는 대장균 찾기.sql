# https://school.programmers.co.kr/learn/courses/30/lessons/301647
SELECT C.id, C.genotype, P.genotype AS parent_genotype
FROM ECOLI_DATA C
INNER JOIN ECOLI_DATA P ON C.parent_id = P.id
WHERE C.genotype & P.genotype = P.genotype
ORDER BY 1;
