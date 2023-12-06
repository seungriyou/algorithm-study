# https://www.acmicpc.net/problem/2407
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# dp[i][j] = jCi, j개 원소 중 i개 원소를 고르는 조합의 개수
dp = [[0] * (n + 1) for _ in range(m + 1)]

for j in range(1, n + 1):
    dp[1][j] = j

for i in range(1, m + 1):
    dp[i][i] = 1

for i in range(2, m + 1):
    for j in range(2, n + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

print(dp[m][n])
