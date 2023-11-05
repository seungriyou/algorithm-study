# https://www.acmicpc.net/problem/1535
import sys
input = sys.stdin.readline

N = int(input())
cost = [0] + list(map(int, input().split()))
joy = [0] + list(map(int, input().split()))

dp = [[0] * 101 for _ in range(N + 1)]

for i in range(N + 1):      # -- 사람
    for j in range(101):    # -- 임시 체력
        if cost[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + joy[i])

print(dp[N][99])    # -- 체력이 0이 되면 죽는다..!
