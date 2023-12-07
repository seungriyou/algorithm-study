# https://leetcode.com/problems/find-users-with-valid-e-mails/

SELECT *
FROM Users
WHERE mail REGEXP ('^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com');

# ===== (23.12.07) reviewed ====
SELECT *
FROM Users
WHERE mail REGEXP ('^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com');
