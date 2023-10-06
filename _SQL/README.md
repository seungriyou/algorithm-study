# SQL CheatSheet 🔖

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

## 2. Functions
### 2.1 `GROUP_CONCAT`: GROUP BY 시, 문자열 CONCAT 하기
> https://leetcode.com/problems/group-sold-products-by-the-date/

**`GROUP_CONCAT`** 함수를 이용한다.

내부에 `DISTINCT`, `ORDER BY [컬럼명]`, `SEPERATOR` 등을 모두 적용할 수 있다.

```sql
SELECT 
    sell_date
    , COUNT(DISTINCT product) AS num_sold
    , GROUP_CONCAT(DISTINCT product SEPARATOR '&') AS products    # -- ORDER BY product 할 필요 없음
FROM Activities
GROUP BY sell_date
ORDER BY sell_date, product;
```

<br>

### 2.2 `DATE_FORMAT`: DATE format을 다루는 방법
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

| Pattern     | What the Pattern matches                                                                                                                                                         |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `*`         | Zero or more instances of string preceding it                                                                                                                                    |
| `+`         | One or more instances of strings preceding it                                                                                                                                    |
| `.`         | Any single character                                                                                                                                                             |
| `?`         | Match zero or one instances of the strings preceding it                                                                                                                          |
| `^` (caret) | Beginning of string                                                                                                                                                              |
| `$`         | End of string                                                                                                                                                                    |
| `[abc]`     | Any character listed between the square brackets                                                                                                                                 |
| `[^abc]`    | Any character not listed between the square brackets                                                                                                                             |
| `[A-Z]`     | match any upper case letter                                                                                                                                                      |
| `[a-z]`     | match any lower case letter                                                                                                                                                      |
| `[0-9]`     | match any digit from 0 through to 9                                                                                                                                              |
| `[[:<:]]`   | matches the beginning of words                                                                                                                                                   |
| `[[:>:]]`   | matches the end of words                                                                                                                                                         |
| `[:class:]` | matches a character class<br>- `[:alpha:]` to match letters<br>- `[:space:]` to match white space<br>- `[:punct:]` is match punctuations<br>- `[:upper:]` for upper class letters |
| `p1ㅣp2ㅣp3`  | Alternation; matches any of the patterns p1, p2, or p3 |
| `{n}`       | n instances of preceding element                                                                                                                                                 |
| `{m,n}`     | m through n instances of preceding element                                                                                                                                       |


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
