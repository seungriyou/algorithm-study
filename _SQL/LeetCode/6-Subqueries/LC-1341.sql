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

# ===== (23.12.08) reviewed =====
(
    SELECT name AS results
    FROM MovieRating
    INNER JOIN Users USING(user_id)
    GROUP BY user_id
    ORDER BY COUNT(movie_id) DESC, name
    LIMIT 1
)
UNION ALL   # movie title user name이 같은 경우를 위해 union all
(
    SELECT title AS results
    FROM MovieRating
    INNER JOIN Movies USING(movie_id)
    WHERE DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
    GROUP BY movie_id
    ORDER BY AVG(rating) DESC, title
    LIMIT 1
);
