# https://leetcode.com/problems/movie-rating/

(
    SELECT name AS results
    FROM MovieRating R
    INNER JOIN Users U ON R.user_id = U.user_id
    GROUP BY R.user_id
    ORDER BY COUNT(*) DESC, name
    LIMIT 1
)
UNION ALL
(
    SELECT title AS results
    FROM MovieRating R
    INNER JOIN Movies M ON R.movie_id = M.movie_id
    WHERE DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
    GROUP BY R.movie_id
    ORDER BY AVG(rating) DESC, title
    LIMIT 1
);
