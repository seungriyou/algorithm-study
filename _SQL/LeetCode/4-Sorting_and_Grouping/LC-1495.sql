-- https://leetcode.com/problems/friendly-movies-streamed-last-month/

SELECT DISTINCT title
FROM TVProgram
INNER JOIN Content USING(content_id)
WHERE YEAR(program_date) = 2020 AND MONTH(program_date) = 6 AND kids_content = "Y" AND content_type = "Movies";
