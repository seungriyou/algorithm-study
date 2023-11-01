# https://www.acmicpc.net/problem/11722
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.reverse()  # 가장 긴 감소하는 부분 수열을 구해야 하므로, 뒤집어서 가장 긴 증가하는 부분 수열 구해보기

dp = [1] * N    # # dp[i] = nums[i]가 포함된 가장 긴 증가하는 부분 수열 (LIS)

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        # if nums[j] < nums[i] and dp[i] < dp[j] + 1:
        #     dp[i] = dp[j] + 1

print(max(dp))
