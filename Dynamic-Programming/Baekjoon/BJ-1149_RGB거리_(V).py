# https://www.acmicpc.net/problem/1149
import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]    # dp[i][j]: 집 i를 j 색깔로 칠할 때, 현재까지의 비용

dp[0] = costs[0]
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

print(min(dp[-1]))
