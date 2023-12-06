# https://www.acmicpc.net/problem/17626
import sys
input = sys.stdin.readline

n = int(input())

# ==== DP (pypy3 통과) ====
dp = [0, 1]

for i in range(2, n + 1):
    min_v = int(1e9)
    s = 1

    while s * s <= i:
        min_v = min(min_v, dp[i - s * s])
        s += 1

    dp.append(min_v + 1)

print(dp[n])

# ==== Brute Force (Python3 통과) ====
def get_min_num(n):
    is_power_num = [True if int(i ** 0.5) ** 2 == i else False for i in range(n + 1)]

    # 제곱수일 때
    if is_power_num[n]:
        return 1

    # 제곱수를 뺀 것이 제곱수일 때
    for i in range(1, int(n ** 0.5) + 1):
        if is_power_num[n - i * i]:
            return 2

    # 제곱수를 뺀 것에서 다시 한 번 더 제곱수를 뺀 것이 제곱수일 때
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(1, int((n - i * i) ** 0.5) + 1):
            if is_power_num[n - i * i - j * j]:
                return 3

    # 위의 경우에 속하지 않는다면, 최대 수인 4 반환
    return 4

print(get_min_num(n))
