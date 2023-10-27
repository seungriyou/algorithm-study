# [BOJ] 2839 - 설탕 배달
# https://www.acmicpc.net/problem/2839

n = int(input())
INF = int(1e9)
dp = [INF] * (n + 1)

dp[3] = 1
if n >= 5:
    dp[5] = 1
    for i in range(5, n + 1):
        if dp[i - 3] != INF or dp[i - 5] != INF:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1

if dp[n] < INF:
    print(dp[n])
else:
    print(-1)
