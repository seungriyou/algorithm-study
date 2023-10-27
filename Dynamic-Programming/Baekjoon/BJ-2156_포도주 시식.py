# https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline

n = int(input())
wines = [0] * 3
for _ in range(n):
    wines.append(int(input()))

dp = [0] * (n + 3)

# dp[i]: i 번째 포도주까지의 최대 포도주 양
# dp[0] = wines[0]
# if n > 1:
#     dp[1] = wines[0] + wines[1]
# if n > 2:
#     dp[2] = max(dp[0], dp[1])

for i in range(3, n + 3):
    # 1. i 번째 포도주를 마시는 경우
    # 1.1 i - 1 번째 포도주를 마시지 않는 경우   => dp[i - 2] + wines[i]
    # 1.2 i - 1 번째 포도주를 마시는 경우       => dp[i - 3] + wines[i - 1] + wines[i]
    dp[i] = max(dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])

    # 2. i 번째 포도주를 마시지 않는 경우    => dp[i - 1]와 비교해서 큰 값 선택
    dp[i] = max(dp[i - 1], dp[i])

print(dp[-1])
