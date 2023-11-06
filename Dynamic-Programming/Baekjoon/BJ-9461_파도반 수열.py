# https://www.acmicpc.net/problem/9461
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    # dp = [0] * 101
    # dp[1] = dp[2] = dp[3] = 1
    dp = [0, 1, 1, 1]

    for i in range(3, N + 1):
        # dp[i] = dp[i - 3] + dp[i - 2]
        dp.append(dp[i - 2] + dp[i - 1])
    print(dp[N])
