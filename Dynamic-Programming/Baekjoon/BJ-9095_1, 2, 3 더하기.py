# [BJ] 9095 - 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

max_n = max(nums)
dp = [-1] * (max_n + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_n + 1):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for n in nums:
    print(dp[n])
