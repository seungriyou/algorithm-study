# https://leetcode.com/problems/patients-with-a-condition/

# SELECT *
# FROM Patients
# WHERE conditions REGEXP ('^DIAB1|[ ]DIAB1');

# SELECT *
# FROM Patients
# WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%';

SELECT *
FROM Patients
WHERE conditions REGEXP ('\\bDIAB1');
