# https://www.acmicpc.net/problem/11055
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = nums[:]    # # dp[i] = nums[i]가 포함된 합이 가장 큰 증가하는 부분 수열

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])
        # if nums[j] < nums[i] and dp[i] < dp[j] + nums[i]:
        #     dp[i] = dp[j] + nums[i]

print(max(dp))
