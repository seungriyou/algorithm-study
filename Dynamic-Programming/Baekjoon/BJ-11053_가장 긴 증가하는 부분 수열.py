# [BOJ] 11053 - 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N    # dp[i] = nums[i]가 포함된 가장 긴 증가하는 부분 수열 (LIS)

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
