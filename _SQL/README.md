# MySQL CheatSheet 🔖
> LeetCode, Programmers SQL 문제 풀이 중 새롭게 알게된 것들

<br>

> [!IMPORTANT]
> 조건에 맞는 ID를 기반으로 counting 할 때는 `DISTINCT`를 잊지 말자!!

<br>

## 1. Tips
### 1.1 GROUP BY 후 조건에 부합하는 값 COUNT 하는 방법
> https://leetcode.com/problems/queries-quality-and-percentage/

**`IF()`** 나 **`CASE`-`WHEN`-`THEN`-(`ELSE`)-`END`** 절로 조건을 걸 수 있다.

혹은 비교연산자 자체가 0, 1 값을 반환하므로 그대로 `SUM`, `AVG` 연산에 이용해도 된다.

```sql
SELECT query_name
, ROUND(AVG(rating / position), 2) AS quality
# == 4가지 방법 ==
, ROUND(COUNT(CASE WHEN rating < 3 THEN 1 END) / COUNT(*) * 100, 2) AS poor_query_percentage
, ROUND(SUM(IF(rating < 3, 1, 0)) / COUNT(*) * 100, 2) AS poor_query_percentage
, ROUND(SUM(rating < 3) / COUNT(*) * 100, 2) AS poor_query_percentage
, ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name
```

<br>

### 1.2 결과가 비어있을 때 NULL을 반환하는 방법
> https://leetcode.com/problems/biggest-single-number/

일반 SELECT를 사용하면 결과가 없는 경우는 아예 출력되지 않으므로, **중첩 SELECT 문**을 사용한다.

```sql
SELECT MAX(num) as num
FROM (
    SELECT *
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS N;
```
```sql
SELECT (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
    ORDER BY num DESC LIMIT 1
) AS num;
```

> https://leetcode.com/problems/second-highest-salary/

이렇게 `SELECT` 절 안에 subquery를 넣게 되면, **결과 값이 없는 경우에도 빈 테이블이 아닌 `NULL`을 반환**한다.

```sql
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1, 1
) AS SecondHighestSalary;
```

<br>

### 1.3 FROM 절에 중첩 SELECT 문 사용하는 예제
> https://leetcode.com/problems/delete-duplicate-emails/

GROUP BY 후 함수를 적용한 결과를 WHERE 조건으로 사용하고 싶다면 **중첩 SELECT 문**을 작성한다.

```sql
DELETE FROM Person
WHERE id NOT IN (
    SELECT min_id
    FROM (
        SELECT MIN(id) AS min_id
        FROM Person
        GROUP BY email
    ) M
);
```

<br>

### 1.4 두 테이블의 Cartesian Product 구하기 (JOIN)
> https://leetcode.com/problems/students-and-examinations/

모든 경우의 수를 가지는 두 table의 Cartesian Product는 다음의 세 가지 방법으로 구할 수 있다.

#### [1] Tables

Students

```sql
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
```

Subjects

```sql
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
```

#### [2] Three Ways to Cartesian Product

1. `CROSS JOIN` 사용하기
    
    ```sql
    SELECT *
    FROM Students
    CROSS JOIN Subjects
    ```
    
2. `(INNER) JOIN` 사용하기
    
    ```sql
    SELECT *
    FROM Students
    INNER JOIN Subjects ON 1=1 # -- 1=1은 항상 True임을 나타내어 아무것도 제거하지 않는다는 의미
    ```
    
3. `FROM` 절에 나열하기
    
    ```sql
    SELECT *
    FROM Students, Subjects
    ```


> [!IMPORTANT]  
> 2, 3번 방법의 경우, `ON` 또는 `WHERE` 조건을 설정하면 INNER JOIN으로 동작한다.


```sql
| student_id | student_name | subject_name |
| ---------- | ------------ | ------------ |
| 1          | Alice        | Programming  |
| 1          | Alice        | Physics      |
| 1          | Alice        | Math         |
| 2          | Bob          | Programming  |
| 2          | Bob          | Physics      |
| 2          | Bob          | Math         |
| 13         | John         | Programming  |
| 13         | John         | Physics      |
| 13         | John         | Math         |
| 6          | Alex         | Programming  |
| 6          | Alex         | Physics      |
| 6          | Alex         | Math         |
```

<br>

### 1.5 테이블 내의 데이터 개수 구하기
> https://leetcode.com/problems/game-play-analysis-iv/

`(SELECT COUNT(*) FROM Product)` 와 같이 `COUNT()`를 SELECT 하면 된다.

`(SELECT COUNT(DISTINCT player_id) FROM Activity)` 와 같이 `DISTINCT`를 `COUNT()` 내에 사용할 수도 있다.

```sql
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
```

```sql
SELECT ROUND(COUNT(player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, event_date) IN (
    SELECT player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
    FROM Activity
    GROUP BY player_id
);
```

<br>

### 1.6 조건에 맞는 값 COUNT 하는 방법 (`SUM(condition)`)
> https://leetcode.com/problems/count-salary-categories/

어떤 조건에 부합하는 값의 개수를 세려면, 다음의 두 방법을 사용할 수 있다.

1. **`WHERE` 절에 조건**을 달고, **`SELECT` 절에서 `COUNT(*)` 함수**를 사용한다.
    
    ```sql
    SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count
    FROM Accounts
    WHERE income < 20000
    UNION
    SELECT 'Average Salary' AS category, COUNT(*) AS accounts_count
    FROM Accounts
    WHERE income BETWEEN 20000 AND 50000
    UNION
    SELECT 'High Salary' AS category, COUNT(*) AS accounts_count
    FROM Accounts
    WHERE income > 50000;
    ```
    
2. **`SELECT` 절**에서 **`SUM(condition)` 함수**를 사용하여, condition을 만족하는 값의 개수를 센다.
    
    ```sql
    SELECT 'Low Salary' AS category, SUM(income < 20000) AS accounts_count
    FROM Accounts
    UNION
    SELECT 'Average Salary' AS category, SUM(income BETWEEN 20000 AND 50000) AS accounts_count
    FROM Accounts
    UNION
    SELECT 'High Salary' AS category, SUM(income > 50000) AS accounts_count
    FROM Accounts;
    ```

<br>

### 1.7 특정 attribute 값이 최소/최대인 row 반환하기
> https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

해당 attribute를 기준으로 `ORDER BY` 후, `LIMIT 1`을 걸어준다.

```sql
SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id
    FROM RequestAccepted
) AS R
GROUP BY id
ORDER BY num DESC
LIMIT 1;
```

> [!IMPORTANT]
> 추가 자료: https://dev.mysql.com/doc/refman/8.0/en/example-maximum-row.html

<br>

### 1.8 `WITH` 절: 가상테이블 만들기
> https://leetcode.com/problems/restaurant-growth/

`WITH` 절로 가상테이블을 생성하면 동일한 서브쿼리를 반복해서 쓰지 않을 수 있다.

```sql
WITH C AS (
    SELECT visited_on, SUM(amount) AS day_amount 
    FROM Customer 
    GROUP BY visited_on
)

SELECT C1.visited_on, SUM(C2.day_amount) AS amount, ROUND(SUM(C2.day_amount) / 7, 2) AS average_amount
FROM C C1, C C2
WHERE 
    C1.visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM Customer), INTERVAL 6 DAY)
    AND DATEDIFF(C1.visited_on, C2.visited_on) BETWEEN 0 AND 6 
GROUP BY C1.visited_on
ORDER BY C1.visited_on;
```

<br>

### 1.9 어떤 문자열의 앞부분에 위치한 숫자 추출하기
> https://school.programmers.co.kr/learn/courses/30/lessons/151141

`30일 이상`이라는 문자열에서 **`30`이라는 숫자를 추출**하려면, 다음과 같이 **`CAST()`나 `CONVERT()`를 이용하여 데이터 타입 변환을 수행**하면 된다.

```sql
SELECT CAST('30일 이상' AS UNSIGNED); # 30
```

```sql
SELECT CONVERT('30일 이상', UNSIGNED); # 30
```

이러한 경우, `UNSIGNED`가 아닌 `일 이상`은 삭제된다.

하지만, 이러한 함수들은 **앞에서부터 순차적으로 데이터 타입 변환을 수행하다가 변환이 불가능한 경우 중단**되므로, 다음과 같은 경우에 대해서는 주의하자.

```sql
SELECT CAST('~ 30일 이상' AS UNSIGNED); # 0
SELECT CONVERT('~ 30일 이상', UNSIGNED); # 0
```

```sql
SELECT CAST('30일123 이상' AS UNSIGNED); # 30
SELECT CONVERT('30일123 이상', UNSIGNED); # 30
```

<br>

### 1.10 `LIMIT`을 Subquery에 사용하는 방법
> https://school.programmers.co.kr/learn/courses/30/lessons/164671

다음과 같이 서브쿼리 내에서 `LIMIT`을 사용하여 `IN` 연산을 수행하면 오류가 발생한다.

```sql
SELECT CONCAT(file_id, file_name, file_ext)) AS file_path
FROM USED_GOODS_FILE
WHERE board_id IN (
    SELECT board_id
    FROM USED_GOODS_BOARD
    ORDER BY views DESC
    LIMIT 5 # top 5
)
ORDER BY file_id DESC;
```

> [!Warning]  
> **`LIMIT` & `IN`/`ALL`/`ANY`/`SOME` subquery**를 지원하지 않는다는 오류가 발생한다.

하지만, 서브쿼리 내에서 `LIMIT`으로 제한할 row 개수가 `1`보다 크다면 다음과 같이 **alias를 활용**하면 된다.

```sql
SELECT CONCAT(file_id, file_name, file_ext)) AS file_path
FROM USED_GOODS_FILE
WHERE board_id IN (
    SELECT *
    FROM (
        SELECT board_id
        FROM USED_GOODS_BOARD
        ORDER BY views DESC
        LIMIT 5 # top 5
    ) AS B
)
ORDER BY file_id DESC;
```

물론, 서브쿼리 내에서 `LIMIT`으로 제한할 row 개수가 `1`이라면 `IN` 연산 대신 `=`를 사용하면 되긴 하다.

```sql
WHERE board_id = (
    SELECT board_id
    FROM USED_GOODS_BOARD
    ORDER BY views DESC
    LIMIT 1
)
```

<br>

### 1.11 `WITH RECURSIVE` 문: 재귀 쿼리
> https://school.programmers.co.kr/learn/courses/30/lessons/59413
> https://dev.mysql.com/doc/refman/8.0/en/with.html
> https://inpa.tistory.com/entry/MYSQL-%F0%9F%93%9A-RECURSIVE-%EC%9E%AC%EA%B7%80-%EC%BF%BC%EB%A6%AC
> https://umanking.github.io/2021/07/13/mysql-cte/

#### CTE (Common Table Expression)

- 임시로 쿼리 결과를 저장해놓고, 여러 번 참조해서 사용하는 용도이다.
- `WITH` 문을 통해 CTE를 정의할 수 있다.
    
    ```sql
    WITH
      cte1 AS (SELECT a, b FROM table1),
      cte2 AS (SELECT c, d FROM table2)
    SELECT b, d FROM cte1 JOIN cte2
    WHERE cte1.a = cte2.c;
    ```
    

##### `WITH` 문

```sql
with_clause:
    WITH [RECURSIVE]
        cte_name [(col_name [, col_name] ...)] AS (subquery)
        [, cte_name [(col_name [, col_name] ...)] AS (subquery)] ...
```

- column name은 괄호 `()` 안에 나열하거나, 혹은 `subquery` 파트의 첫 번째 `SELECT` 문에서 가져온다.
    
    ```sql
    with_clause:
        WITH [RECURSIVE]
            cte_name [(col_name [, col_name] ...)] AS (subquery)
            [, cte_name [(col_name [, col_name] ...)] AS (subquery)] ...
    ```
    
    ```sql
    WITH cte AS
    (
      SELECT 1 AS col1, 2 AS col2
      UNION ALL
      SELECT 3, 4
    )
    SELECT col1, col2 FROM cte;
    ```
    

#### RECURSIVE CTE

##### `WITH RECURSIVE` 문

recursive CTE는 `WITH RECURSIVE` 문으로 생성하며, `subquery` 부분은 기본적으로 다음과 같은 구조를 가진다.

```sql
SELECT ...      -- return initial row set
UNION ALL
SELECT ...      -- return additional row sets
```

예시는 다음과 같다.

```sql
WITH RECURSIVE cte (n) AS
(
	-- Non-Recursive (첫번째 루프에서만 실행됨)
  SELECT 1
  UNION ALL
	-- Recursive (읽어 올 때마다 행의 위치가 기억되어 다음번 읽어 올 때 다음 행으로 이동함)
  SELECT n + 1 FROM cte WHERE n < 5
)
SELECT * FROM cte;
```

```sql
+------+
| n    |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    5 |
+------+
```

만약 CTE의 recursive part가 점점 길어지는 column을 반환한다면, nonrecursive part의 column의 길이를 `CAST()` 함수를 통해 늘려야 한다.

- `CAST()` 함수 사용 X
    
    ```sql
    WITH RECURSIVE cte AS
    (
      SELECT 1 AS n, 'abc' AS str
      UNION ALL
      SELECT n + 1, CONCAT(str, str) FROM cte WHERE n < 3
    )
    SELECT * FROM cte;
    ```
    
    ```sql
    +------+------+
    | n    | str  |
    +------+------+
    |    1 | abc  |
    |    2 | abc  |
    |    3 | abc  |
    +------+------+
    ```
    
- `CAST()` 함수 사용 O
    
    ```sql
    WITH RECURSIVE cte AS
    (
      SELECT 1 AS n, **CAST('abc' AS CHAR(20))** AS str
      UNION ALL
      SELECT n + 1, CONCAT(str, str) FROM cte WHERE n < 3
    )
    SELECT * FROM cte;
    ```
    
    ```sql
    +------+--------------+
    | n    | str          |
    +------+--------------+
    |    1 | abc          |
    |    2 | abcabc       |
    |    3 | abcabcabcabc |
    +------+--------------+
    ```
    

recursive CTE subquery 부분에서는 다음의 것들이 들어가서는 안 된다.

- Aggregate functions such as `SUM()`
- Window functions
- `GROUP BY`
- `ORDER BY`
- `DISTINCT`

<br>

### 1.12 FULL OUTER JOIN
> https://leetcode.com/problems/employees-with-missing-information/

<img src="https://github.com/seungriyou/algorithm-study/assets/43572543/406cfdbe-446c-4003-8ba6-e1da8a80b31f" width="30%" />

MySQL은 **FULL OUTER JOIN**을 native 하게 지원하지 않으므로, `LEFT JOIN`, `RIGHT JOIN`, `UNION`을 활용하여 구현할 수 있다.

다음과 같은 두 개의 테이블을 **FULL OUTER JOIN** 해보자!

```
Employees table:
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 2           | Crew     |
| 4           | Haven    |
| 5           | Kristian |
+-------------+----------+

Salaries table:
+-------------+--------+
| employee_id | salary |
+-------------+--------+
| 5           | 76071  |
| 1           | 22517  |
| 4           | 63539  |
+-------------+--------+
```

#### [1] column 순서 맞추지 않기

`UNION` 시에는 첫 번째 결과에서 column 이름이 정해지기 때문에, 다음과 같이 column이 섞이게 된다. (하지만 조건으로 거르기만 하려면 큰 문제가 없다.)

```sql
SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
UNION 
SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id)

| employee_id | name     | salary   |
| ----------- | -------- | -------- |
| 2           | Crew     | null     |
| 4           | Haven    | 63539    |
| 5           | Kristian | 76071    |
| 5           | 76071    | Kristian |
| 1           | 22517    | null     |
| 4           | 63539    | Haven    |
```

이때, `UNION`으로 이어진 각각의 SQL문 결과를 살펴보면 다음과 같다.

```sql
SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)

| employee_id | name     | salary |
| ----------- | -------- | ------ |
| 2           | Crew     | null   |
| 4           | Haven    | 63539  |
| 5           | Kristian | 76071  |
```

```sql
SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id)

| employee_id | salary | name     |
| ----------- | ------ | -------- |
| 5           | 76071  | Kristian |
| 1           | 22517  | null     |
| 4           | 63539  | Haven    |
```

#### [2] column 순서 맞춰주기

`SELECT` 시 column의 순서를 동일하게 맞춰준다면, 다음과 같이 깔끔한 `FULL OUTER JOIN`을 얻을 수 있다.

```sql
SELECT employee_id, name, salary FROM Employees LEFT JOIN Salaries USING(employee_id)
UNION 
SELECT employee_id, name, salary FROM Employees RIGHT JOIN Salaries USING(employee_id)

| employee_id | name     | salary |
| ----------- | -------- | ------ |
| 2           | Crew     | null   |
| 4           | Haven    | 63539  |
| 5           | Kristian | 76071  |
| 1           | null     | 22517  |
```

<br>

### 1.13 `GROUP BY` 후 특정 Column의 `MAX` 값에 해당하는 Row 찾기

`GROUP BY`를 수행한 후, 특정 column의 `MAX` 값에 해당하는 row를 찾고 싶다면 다음의 방법 중 하나를 이용하면 된다.

> https://leetcode.com/problems/product-sales-analysis-iii/

1. **subquery**
    
    ```sql
    SELECT product_id, year AS first_year, quantity, price
    FROM Sales
    WHERE (product_id, year) IN (
        SELECT product_id, MIN(year)
        FROM Sales
        GROUP BY 1
    );
    ```
    
2. **윈도우 함수 `RANK()` → 그 값이 1인 행 찾기**
    
    ```sql
    SELECT product_id, year AS first_year, quantity, price
    FROM (
        SELECT *, RANK() OVER(PARTITION BY product_id ORDER BY year) AS _rank
        FROM Sales
    ) S
    WHERE _rank = 1;
    ```

<br>

> https://school.programmers.co.kr/learn/courses/30/lessons/131123

1. **subquery**
    
    ```sql
    SELECT food_type, rest_id, rest_name, favorites
    FROM REST_INFO
    WHERE (food_type, favorites) IN (
        SELECT food_type, MAX(favorites)
        FROM REST_INFO
        GROUP BY food_type
    )
    ORDER BY 1 DESC;
    ```
    
2. **윈도우 함수 `RANK()` → 그 값이 1인 행 찾기**
    
    ```sql
    SELECT food_type, rest_id, rest_name, favorites
    FROM (
        SELECT *, RANK() OVER (PARTITION BY food_type ORDER BY favorites DESC) AS _rank
        FROM REST_INFO
    ) R
    WHERE _rank = 1
    ORDER BY 1 DESC;
    ```

<br>

### 1.14 `SELECT` 절에서 생성한 Column을 `HAVING` 절에서 사용해도 되는가?
> https://dev.mysql.com/doc/refman/8.0/en/select.html

![image](https://github.com/seungriyou/algorithm-study/assets/43572543/e0eebd9d-0de5-429a-87a2-7c9ee6620f4d)

**SQL 표준**에서 `HAVING` 절은 **`GROUP BY` 절**이나 **aggregate function에서 사용된 column만** 참조하도록 요구하지만, 

**MySQL**에서 `HAVING` 절은 **`SELECT` 절**이나 **outer subqueries에 있는 columns**도 참조 가능하다.

결론적으로, `SELECT` 절에서 생성한 Column을 `HAVING` 절에서 사용해도 된다!

> https://leetcode.com/problems/list-the-products-ordered-in-a-period/

그래서 다음과 같이 기존의 `unit` column에 aggregate function을 씌워 새롭게 alias를 `unit`이라는 이름으로 부여한 column을 `HAVING` 절에 사용할 수 있는 것이다.

```sql
SELECT product_name, SUM(unit) AS unit
FROM Orders
INNER JOIN Products USING(product_id)
WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'
GROUP BY product_id
HAVING unit >= 100;
```

<br>

### 1.15 3개 이상의 Row에서 id 값이 연속된 값으로 나타나는 부분 추출하기
> https://leetcode.com/problems/human-traffic-of-stadium/

주어진 `Stadium` 테이블의 구조는 다음과 같다.

```
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
```

`Stadium` 테이블에서

1. 연속된 `id` 값이 3개 이상의 row에서 나타나면서
2. 각 레코드의 `people`이 100 이상인

레코드들을 다음과 같이 반환하는 방법을 알아보자.

```
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
```

우선, 2번 조건(**`people` ≥ 100**)을 만족하는 레코드들만 추출하면 다음과 같다.

```sql
SELECT *
FROM Stadium
WHERE people >= 100

| id | visit_date | people |
| -- | ---------- | ------ |
| 2  | 2017-01-02 | 109    |
| 3  | 2017-01-03 | 150    |
| 5  | 2017-01-05 | 145    |
| 6  | 2017-01-06 | 1455   |
| 7  | 2017-01-07 | 199    |
| 8  | 2017-01-09 | 188    |
```

여기에서 1번 조건을 만족하는 레코드를 찾기 위해 **“연속된 `id` 값”** 이 나타나는 부분을 표시하려면 어떻게 해야할까?

바로 윈도우 함수인 `ROW_NUMBER()`를 이용하여, `id - ROW_NUMBER()` 값을 통해 해당 부분을 표시할 수 있다.

연속된 `id` 값이 나타나는 부분 내에서는 해당 값이 동일할 것이기 때문에, column의 이름을 `_group`이라고 정할 수 있을 것이다.

```sql
SELECT
    *,
    id - ROW_NUMBER() OVER (ORDER BY id) AS _group
FROM Stadium
WHERE people >= 100

| id | visit_date | people | _group |
| -- | ---------- | ------ | ------ |
| 2  | 2017-01-02 | 109    | 1      |
| 3  | 2017-01-03 | 150    | 1      |
| 5  | 2017-01-05 | 145    | 2      |
| 6  | 2017-01-06 | 1455   | 2      |
| 7  | 2017-01-07 | 199    | 2      |
| 8  | 2017-01-09 | 188    | 2      |
```

이렇게 생성한 테이블을 CTE로 선언해두면, 다음과 같이 `WHERE` 절에서 `GROUP BY`를 이용하여 1번 조건의 **“3개 이상의 row”** 조건도 만족하는 레코드들을 추출할 수 있다.

```sql
WITH T AS (
    SELECT
        *,
        id - ROW_NUMBER() OVER (ORDER BY id) AS _group
    FROM Stadium
    WHERE people >= 100
)

SELECT id, visit_date, people
FROM T
WHERE _group IN (
    SELECT _group
    FROM T
    GROUP BY _group
    HAVING COUNT(id) >= 3
);

| id | visit_date | people |
| -- | ---------- | ------ |
| 5  | 2017-01-05 | 145    |
| 6  | 2017-01-06 | 1455   |
| 7  | 2017-01-07 | 199    |
| 8  | 2017-01-09 | 188    |
```

<br>

## 2. Functions
### 2.1 `GROUP_CONCAT`: GROUP BY 시, 문자열 CONCAT 하기
> https://leetcode.com/problems/group-sold-products-by-the-date/

**`GROUP_CONCAT`** 함수를 이용한다.

내부에 `DISTINCT`, `ORDER BY [컬럼명]`, `SEPERATOR` 등을 모두 적용할 수 있다.

```sql
SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY 1;
```

default separator는 `,`이므로, `,`를 이용하고 싶다면 다음과 같이 `SEPARATOR`를 생략해도 된다.

```python
GROUP_CONCAT(DISTINCT product ORDER BY product) AS products     # default separator = ','
```

<br>

### 2.2 `DATE_FORMAT`: DATE Format을 다루는 방법
> https://leetcode.com/problems/monthly-transactions-i/

`2018-12-18` 과 같은 DATE 형식에서 **YEAR + MONTH를 추출**하고 싶을 때, 다음과 같은 방법을 선택할 수 있다.

1. 문자열이라고 생각하고 `LEFT()` 사용하기
    
    ```sql
    LEFT(trans_date, 7) AS month
    ```
    
2. `DATE_FORMAT` 함수 사용하기
    
    ```sql
    DATE_FORMAT(trans_date, '%Y-%m') AS month
    ```

```sql
SELECT 
    # LEFT(trans_date, 7) AS month
    DATE_FORMAT(trans_date, '%Y-%m') AS month
    , country
    , COUNT(*) AS trans_count
    , SUM(IF(state = 'approved', 1, 0)) AS approved_count
    , SUM(amount) AS trans_total_amount
    , SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY country, month
```

| Specifier | Description                                                                                        |
| --- |----------------------------------------------------------------------------------------------------|
| `%a` | Abbreviated weekday name (`Sun`..`Sat`)                                                            |
| `%b` | Abbreviated month name (`Jan`..`Dec`)                                                              |
| `%c` | Month, numeric (`0`..`12`)                                                                         |
| `%D` | Day of the month with English suffix (`0th`, `1st`, `2nd`, `3rd`, …)                               |
| `%d` | Day of the month, numeric (`00`..`31`)                                                             |
| `%e` | Day of the month, numeric (`0`..`31`)                                                              |
| `%f` | Microseconds (`000000`..`999999`)                                                                  |
| `%H` | Hour (`00`..`23`)                                                                                  |
| `%h` | Hour (`01`..`12`)                                                                                  |
| `%I` | Hour (`01`..`12`)                                                                                  |
| `%i` | Minutes, numeric (`00`..`59`)                                                                      |
| `%j` | Day of year (`001`..`366`)                                                                         |
| `%k` | Hour (`0`..`23`)                                                                                   |
| `%l` | Hour (`1`..`12`)                                                                                   |
| `%M` | Month name (`January`..`December`)                                                                 |
| `%m` | Month, numeric (`00`..`12`)                                                                        |
| `%p` | `AM` or `PM`                                                                                       |
| `%r` | Time, 12-hour (`hh:mm:ss` followed by `AM` or `PM`)                                                |
| `%S` | Seconds (`00`..`59`)                                                                               |
| `%s` | Seconds (`00`..`59`)                                                                               |
| `%T` | Time, 24-hour (`hh:mm:ss`)                                                                         |
| `%U` | Week (`00`..`53`), where Sunday is the first day of the week; `WEEK()` mode 0                      |
| `%u` | Week (`00`..`53`), where Monday is the first day of the week; `WEEK()` mode 1                      |
| `%V` | Week (`01`..`53`), where Sunday is the first day of the week; `WEEK()` mode 2; used with `%X`      |
| `%v` | Week (`01`..`53`), where Monday is the first day of the week; `WEEK()` mode 3; used with `%x`      |
| `%W` | Weekday name (`Sunday`..`Saturday`)                                                                |
| `%w` | Day of the week (`0`=Sunday..`6`=Saturday)                                                         |
| `%X` | Year for the week where Sunday is the first day of the week, numeric, four digits; used with `%V`  |
| `%x` | Year for the week, where Monday is the first day of the week, numeric, four digits; used with `%v` |
| `%Y` | Year, numeric, four digits                                                                         |
| `%y` | Year, numeric (two digits)                                                                         |
| `%%` | A literal `%` character                                                                            |
| `%x` | `x`, for any “`x`” not listed above                                                                  |

<br>

### 2.3 `COALESCE`: NULL이 아닌 첫 번째 파라미터 반환 (`IFNULL`과 비교)
> https://leetcode.com/problems/students-and-examinations/

#### [1] `COALESCE(val1, val2, ..., val_n)` 함수

`COALESCE(val1, val2, ..., val_n)`은 파라미터로 받는 value 중 첫 번째 non-null value를 반환한다.

```sql
SELECT COALESCE(NULL, NULL, NULL, 'hi~', NULL, 'bye');

# hi~
```

#### [2] `IFNULL(expression, alt_value)` 과 비교

##### `IFNULL`과 `COALESCE`를 모두 활용할 수 있는 예시

`IFNULL(expression, alt_value)`은 파라미터로 받는 `expression`이 `NULL`인 경우 `alt_value`를 반환하고, `NOT NULL`인 경우 `expression`을 반환한다.

따라서 위의 문제에서 다음은 같은 결과를 도출한다.

```sql
SELECT 
    S.student_id
    , S.student_name
    , Sub.subject_name
    , IFNULL(E.cnt, 0) AS attended_exams
...
```

```sql
SELECT
    S.student_id
    , S.student_name
    , Sub.subject_name
    , COALESCE(E.cnt, 0) AS attended_exams
...
```

##### `IFNULL`과 `COALESCE`의 차이점

- `COALESCE`에는 여러 개의 값을 파라미터로 전달할 수 있다.
- `COALESCE`는 표준 SQL 함수이나, `IFNULL`은 MySQL에서만 제공하는 함수이다.

<br>

### 2.4 문자열 패턴 검색: `LIKE`, `RLIKE`, `REGEXP`
#### [1] `LIKE`: 간단한 패턴 검색
> https://www.w3schools.com/mysql/mysql_like.asp

```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN (NOT) LIKE pattern;
```

| Wildcard | Description | Example |
| --- | --- | --- |
| `%` | 여러 문자와 대응됨 | `a%`: a로 시작하는 문자열<br>`%a`: a로 끝나는 문자열<br>`a%o`: a로 시작하고 o로 끝나는 문자열 |
| `_` | 하나의 문자와 대응됨 | `_r%`: r을 두 번째 문자로 가지는 문자열<br>`a__%`: a로 시작하고 최소 3개의 문자를 가지는 문자열 |


#### [2] `RLIKE` / `REGEXP`: 복잡한 패턴 검색 (w/ 정규표현식)
> https://www.geeksforgeeks.org/rlike-operator-in-mysql/

| Pattern     | What the Pattern Matches                                                                                                                                                          |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `*`         | Zero or more instances of string preceding it                                                                                                                                     |
| `+`         | One or more instances of strings preceding it                                                                                                                                     |
| `.`         | Any single character                                                                                                                                                              |
| `?`         | Match zero or one instances of the strings preceding it                                                                                                                           |
| `^` (caret) | Beginning of string                                                                                                                                                               |
| `$`         | End of string                                                                                                                                                                     |
| `[abc]`     | Any character listed between the square brackets                                                                                                                                  |
| `[^abc]`    | Any character not listed between the square brackets                                                                                                                              |
| `[A-Z]`     | match any upper case letter                                                                                                                                                       |
| `[a-z]`     | match any lower case letter                                                                                                                                                       |
| `[0-9]`     | match any digit from 0 through to 9                                                                                                                                               |
| `[[:<:]]`   | matches the beginning of words                                                                                                                                                    |
| `[[:>:]]`   | matches the end of words                                                                                                                                                          |
| `[:class:]` | matches a character class<br>- `[:alpha:]` to match letters<br>- `[:space:]` to match white space<br>- `[:punct:]` is match punctuations<br>- `[:upper:]` for upper class letters |
| `p1ㅣp2ㅣp3`  | Alternation; matches any of the patterns p1, p2, or p3                                                                                                                            |
| `{n}`       | n instances of preceding element                                                                                                                                                  |
| `{m,n}`     | m through n instances of preceding element                                                                                                                                        |


#### [3] 정규표현식 관련 함수
> https://velog.io/@merci/mySQL-정규식-함수
> 
> https://dev.mysql.com/doc/refman/8.0/en/regexp.html

| Name | Description |
| --- | --- |
| `NOT REGEXP` | Negation of REGEXP |
| `REGEXP` | Whether string matches regular expression |
| `RLIKE` | Whether string matches regular expression |
| `REGEXP_INSTR()` | Starting index of substring matching regular expression |
| `REGEXP_LIKE()` | Whether string matches regular expression |
| `REGEXP_REPLACE()` | Replace substrings matching regular expression |
| `REGEXP_SUBSTR()` | Return substring matching regular expression |

#### [4] 비교
> https://www.sqlines.com/mysql/regexp_rlike

`RLIKE`와 `REGEXP`는 기본적으로 substring을 찾는다. `LIKE`로 substring을 찾으려면 `%` wildcard를 이용한다.

```sql
SELECT name FROM cities WHERE name RLIKE 'A|B|R';
-- or
SELECT name FROM cities WHERE name REGEXP 'A|B|R';
-- or using LIKE
SELECT name FROM cities WHERE name LIKE '%A%' OR name LIKE '%B%' OR name LIKE '%R%'
```

```sql
SELECT name FROM cities WHERE name RLIKE '^A|^B|^R';
-- or
SELECT name FROM cities WHERE name REGEXP '^A|^B|^R';
-- or using LIKE
SELECT name FROM cities WHERE name LIKE 'A%' OR name LIKE 'B%' OR name LIKE 'R%'
```

<br>

### 2.5 `LIMIT`과 `OFFSET`
> https://leetcode.com/problems/second-highest-salary/

그냥 **`LIMIT A`** 를 사용하면 **처음부터 `A` 개의 row를 출력**한다.

```sql
SELECT * FROM 테이블이름 LIMIT 10; # 처음부터 10개 row 출력하기 (1 ~ 10)
```

하지만, **`LIMIT A, B`** 는 **`A` 번째 row에서부터 그 이후 `B` 개의 row를 출력**한다는 뜻이다. 

즉, **`A + 1` 번째 row**부터 **`A + B` 번째 row**까지 출력한다.

```sql
SELECT * FROM 테이블이름 LIMIT 20, 10; # 20번째 row부터 그 이후 10개 row 출력하기 (21 ~ 30)
```

동일한 동작을 **`LIMIT B OFFSET A`** 로 쓸 수도 있다.

```sql
SELECT * FROM 테이블이름 LIMIT 10 OFFSET 20;
```

```sql
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1, 1 # -- 1번째 row부터 그 이후 1개 row == 2번째 row
) AS SecondHighestSalary;
```

<br>

### 2.6 `SUM() OVER()`
> https://leetcode.com/problems/last-person-to-fit-in-the-bus/

특정 column의 누적합을 구해야 할 때 `SUM() OVER()`를 사용할 수 있다.

`turn` column 오름차순 정렬 후 위에서부터 차례로 누적합을 구한다.

```sql
SELECT person_name
FROM (
    SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS sum
    FROM Queue
    ORDER BY sum DESC
) AS Q
WHERE sum <= 1000
LIMIT 1;
```

JOIN을 사용하면 다음과 같이 풀 수도 있다.

```sql
SELECT Q1.person_name
FROM Queue Q1, Queue Q2
WHERE Q1.turn >= Q2.turn
GROUP BY Q1.turn
HAVING SUM(Q2.weight) <= 1000
ORDER BY SUM(Q2.weight) DESC
LIMIT 1;
```

<br>

### 2.7 `PARTITION BY` vs. `GROUP BY`
> https://leetcode.com/problems/investments-in-2016/

> [!IMPORTANT]  
> 추후 추가로 더 정리해야 함!

다음의 두 코드는 같다.

```sql
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
) AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);
```

```sql
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT 
        tiv_2016
        , COUNT(*) OVER(PARTITION BY tiv_2015) AS cnt1
        , COUNT(*) OVER(PARTITION BY lat, lon) AS cnt2
    FROM Insurance
) AS T
WHERE cnt1 > 1 AND cnt2 = 1;
```

<br>

### 2.8 순위 매기기: `RANK()`, `DENSE_RANK()`, `ROW_NUMBER()`
#### 각 함수의 동작 비교
> https://leetcode.com/problems/rank-scores/

각 함수의 동작을 실제 예제로 살펴보자.

```sql
SELECT *,
  RANK() OVER (ORDER BY score DESC) AS _rank,
  DENSE_RANK() OVER (ORDER BY score DESC) AS _dense_rank,
  ROW_NUMBER() OVER (ORDER BY score DESC) AS _row_number
FROM Scores;
```

```sql
| id | score | _rank | _dense_rank | _row_number |
| -- | ----- | ----- | ----------- | ----------- |
| 3  | 4     | 1     | 1           | 1           |
| 5  | 4     | 1     | 1           | 2           |
| 4  | 3.85  | 3     | 2           | 3           |
| 2  | 3.65  | 4     | 3           | 4           |
| 6  | 3.65  | 4     | 3           | 5           |
| 1  | 3.5   | 6     | 4           | 6           |
```

#### SELF JOIN으로 구현해보기
> https://leetcode.com/problems/department-top-three-salaries/

`DENSE_RANK()` 동작을 **SELF JOIN을 사용한 서브쿼리**로 구현할 수도 있다.

다음의 두 코드는 동일한 동작을 수행한다.

```sql
# -- DENSE_RANK()를 WHERE 조건으로 보고싶다면, SELECT 절에서 아예 CASE 문으로 처리
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM (
    SELECT *, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS _rank
    FROM Employee
) AS E
INNER JOIN Department D ON E.departmentId = D.id
WHERE E._rank <= 3;
```

```sql
SELECT D.name AS Department, E1.name AS Employee, E1.salary AS Salary
FROM Employee E1
INNER JOIN Department D ON E1.departmentId = D.id
WHERE (
    SELECT COUNT(DISTINCT E2.salary)
    FROM Employee E2
    WHERE E2.salary > E1.salary AND E2.departmentId = E1.departmentId
) < 3;  # -- 같은 department에서 자신의 salary 보다 높은 salary가 0~2개 존재해야 top3 임!
```

<br>

### 2.9 `CAST()`, `CONVERT()`: 데이터 타입 변환하기
> - https://school.programmers.co.kr/learn/courses/30/lessons/151141
> - https://www.w3schools.com/mysql/func_mysql_cast.asp
> - https://www.w3schools.com/mysql/func_mysql_convert.asp

#### `CAST()` 함수

```sql
CAST(value AS datatype)
```

`datatype`으로 사용할 수 있는 값은 다음과 같다.

| Value |	Description |
| --- | --- |
| `DATE` | 	Converts value to DATE. Format: "YYYY-MM-DD" |
| `DATETIME` | 	Converts value to DATETIME. Format: "YYYY-MM-DD HH:MM:SS" |
| `DECIMAL` | 	Converts value to DECIMAL. Use the optional M and D parameters to specify the maximum number of digits (M) and the number of digits following the decimal point (D). |
| `TIME` | 	Converts value to TIME. Format: "HH:MM:SS" |
| `CHAR` | 	Converts value to CHAR (a fixed length string) |
| `NCHAR` | 	Converts value to NCHAR (like CHAR, but produces a string with the national character set) |
| `SIGNED` | 	Converts value to SIGNED (a signed 64-bit integer) |
| `UNSIGNED` | 	Converts value to UNSIGNED (an unsigned 64-bit integer) |
| `BINARY` | 	Converts value to BINARY (a binary string) |


#### `CONVERT()` 함수

```sql
CONVERT(value, type)

CONVERT(value USING charset)
```

`datatype`으로 사용할 수 있는 값은 다음과 같다. (`CAST()`와 동일)

| Value |	Description |
| --- | --- |
| `DATE` | 	Converts value to DATE. Format: "YYYY-MM-DD" |
| `DATETIME` | 	Converts value to DATETIME. Format: "YYYY-MM-DD HH:MM:SS" |
| `DECIMAL` | 	Converts value to DECIMAL. Use the optional M and D parameters to specify the maximum number of digits (M) and the number of digits following the decimal point (D). |
| `TIME` | 	Converts value to TIME. Format: "HH:MM:SS" |
| `CHAR` | 	Converts value to CHAR (a fixed length string) |
| `NCHAR` | 	Converts value to NCHAR (like CHAR, but produces a string with the national character set) |
| `SIGNED` | 	Converts value to SIGNED (a signed 64-bit integer) |
| `UNSIGNED` | 	Converts value to UNSIGNED (an unsigned 64-bit integer) |
| `BINARY` | 	Converts value to BINARY (a binary string) |

`charset`은 변환하고 싶은 character set(ex. `latin1`)을 명시하면 된다.

<br>

### 2.10 `CONCAT()`, `CONCAT_WS()`: 문자열 이어붙이기
> - https://www.w3schools.com/mysql/func_mysql_concat.asp
> - https://www.w3schools.com/mysql/func_mysql_concat_ws.asp

#### `CONCAT()` 함수

단순히 인자들을 이어붙인다.

```sql
SELECT CustomerName, CONCAT(Address, " ", PostalCode, " ", City) AS Address
FROM Customers;
```

#### `CONCAT_WS()` 함수

첫 번째 인자로 `separator`를 지정할 수 있다.

```sql
SELECT CustomerName, CONCAT_WS(" ", Address, PostalCode, City) AS Address
FROM Customers;
```

<br>

### 2.11 `SUBSTRING()`, `LEFT()`, `RIGHT()`: 부분 문자열 추출하기
> https://www.w3schools.com/mysql/func_mysql_substring.asp

#### `SUBSTRING()` 함수

```sql
SUBSTRING(string, start, length)
SUBSTRING(string FROM start FOR length)
```

- string으로부터 substring의 **시작 지점(`start`)** 과 **길이(`length`)** 를 입력받아 substring을 추출하는 함수이다.
- **시작 지점 (`start`)**
    - 첫 번째 지점은 `1` 이다.
    - 음수를 이용하면 string의 뒤에서부터 찾는다.
- `SUBSTR()` 함수, `MID()` 함수와 동일하다.

#### `LEFT()` 함수
string에서 왼쪽부터 지정된 개수의 문자를 추출한다.

```sql
LEFT(string, number_of_chars)
```

#### `RIGHT()` 함수
string의 오른쪽부터 지정된 개수의 문자를 추출한다.

```sql
RIGHT(string, number_of_chars)
```

<br>

### 2.12 `SUBSTRING_INDEX()`: Delimiter 등장 횟수 기준으로 부분 문자열 추출하기
> https://www.w3schools.com/mysql/func_mysql_substring_index.asp

```sql
SUBSTRING_INDEX(string, delimiter, number)
```

이때, `number`는 `delimiter`를 탐색할 횟수를 의미하며, positive 일수도, negative 일수도 있다.

positive라면 마지막으로 찾은 `delimiter`의 왼쪽을, negative라면 마지막으로 찾은 `delimiter`의 오른쪽을 전부 반환한다.

```sql
SELECT SUBSTRING_INDEX("www.naver.com", ".", 1); # www
SELECT SUBSTRING_INDEX("www.naver.com", ".", 2); # www.naver
SELECT SUBSTRING_INDEX("www.naver.com", ".", 3); # www.naver.com

SELECT SUBSTRING_INDEX("www.naver.com", ".", -1); # com
SELECT SUBSTRING_INDEX("www.naver.com", ".", -2); # naver.com
```

<br>

## 3. About MySQL
### 3.1 쿼리 실행 순서
> - https://milena-pa.medium.com/sql-queries-and-their-order-of-operation-6b7d7ca4d197 
> - https://nohriter.tistory.com/129

#### SQL 쿼리의 실행 순서
![image](https://github.com/seungriyou/algorithm-study/assets/43572543/d2dfd530-7a54-47a5-8246-8d265566a28f)

1. **FROM (+ JOIN)**
2. **WHERE**
3. **GROUP BY**
4. AGGREGATION
5. **HAVING**
6. WINDOW
7. **SELECT**
8. DISTINCT
9. UNION / UNION ALL
10. **ORDER BY**
11. LIMT / OFFSET / FETCH

#### SQL 쿼리의 문법 작성 순서
![image](https://github.com/seungriyou/algorithm-study/assets/43572543/afc93381-b154-4b0f-8b6a-ccda07dc6d38)

1. SELECT
2. FROM
3. WHERE
4. GROUP BY
5. HAVING
6. ORDER BY

<br>

### 3.2 윈도우 함수 총정리 😎
<https://github.com/seungriyou/algorithm-study/issues/1>

<br>

### 3.3 `UNION` 시 Column 순서 및 이름은 어떻게 결정될까?
> https://leetcode.com/problems/rearrange-products-table/

`UNION` 시에는, 첫 번째 쿼리에서 column 이름 및 순서가 결정되므로, 그 이후 쿼리에서는 alias를 설정하지 않아도 된다!

```sql
SELECT product_id, 'store1' AS store, store1 AS price   # -- UNION 시 first query에서 column name 결정하므로, 이후에는 alias 설정 안 해도 ok!
FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2', store2
FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3', store3
FROM Products
WHERE store3 IS NOT NULL;
```
