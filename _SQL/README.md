# SQL Tips
> 나만의 SQL CheatSheet 📃

<br>

### 01. GROUP BY 후 조건에 부합하는 값 COUNT 하는 방법
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

### 02. 결과가 비어있을 때 NULL을 반환하는 방법
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

### 03. FROM 절에 중첩 SELECT 문 사용하는 예제
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

### 04. WHERE 절 조건에 정규 표현식 사용하기
> https://leetcode.com/problems/find-users-with-valid-e-mails/

**`REGEXP`** 를 이용한다.

```sql
SELECT *
FROM Users
WHERE mail REGEXP ('^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com');
```

> https://leetcode.com/problems/patients-with-a-condition/

```sql
SELECT *
FROM Patients
WHERE conditions REGEXP ('\\bDIAB1');
# WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%';
```

<br>

### 05. GROUP BY 시, 문자열 CONCAT 하기
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

### 06. DATE format을 다루는 방법
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
