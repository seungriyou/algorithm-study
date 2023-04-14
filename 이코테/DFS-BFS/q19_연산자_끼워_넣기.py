# https://www.acmicpc.net/problem/14888
# 사칙연산자에 대해서 중복순열(itertools - product)을 이용해서 완전탐색도 가능하지만
# 여기에서는 dfs로 풀어보자

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = int(1e9)
max_value = -int(1e9)

# i = 다음 요소 인덱스, now = 현재까지 계산한 결과
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 요소를 다 본 경우
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        # 각 연산자에 대해 재귀적으로 호출
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 주의!! (음수의 나눗셈)
            div += 1

dfs(1, data[0]) # 다음 인덱스 = 1, 현재 값 = data[0]

print(max_value)
print(min_value)
