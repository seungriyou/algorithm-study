# https://www.acmicpc.net/problem/1010
import sys
from math import factorial
input = sys.stdin.readline

T = int(input())

# ==== combination ====
for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // factorial(M - N) // factorial(N))

# ==== dp ====
dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

for _ in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])

# ==== dp2 ====
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for j in range(1, M + 1):
        dp[1][j] = j
    for i in range(1, N + 1):
        dp[i][i] = 1
    for i in range(2, N + 1):
        for j in range(2, M + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    print(dp[N][M])
