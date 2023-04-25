# [BOJ] 11053 - 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# i 까지의 가장 긴 증가하는 부분 수열
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
