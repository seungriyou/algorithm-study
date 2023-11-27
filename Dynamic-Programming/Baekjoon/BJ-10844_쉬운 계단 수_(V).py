# https://www.acmicpc.net/problem/10844
import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]
# dp[i(=자릿수)][j(=숫자값)] = 해당 조건이 가능한 계단 수의 개수
# j = 0이라면, dp[i][j] = dp[i - 1][1]
# j = 1 ~ 8이라면, dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
# j = 9라면, dp[i][j] = dp[i - 1][8]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1_000_000_000)
