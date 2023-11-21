# https://www.acmicpc.net/problem/1912
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


# ===== 1D DP =====
dp = [0] * N    # dp[i]: nums[:i+1]까지 봤을 때, nums[i]가 포함된 연속 구간의 합 중 가장 큰 값
dp[0] = nums[0]

for i in range(1, N):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])   # 자기자신 or 이전까지의 최대 연속구간 합 + 자기자신 중 큰 값

print(max(dp))


# ===== O(1) Space DP =====
prev = max_val = nums[0]    # 이전 숫자가 포함된 연속 구간 합 중 가장 큰 값 tracking

for i in range(1, N):
    if prev <= 0:
        prev = nums[i]
    else:
        prev += nums[i]
    max_val = max(max_val, prev)

print(max_val)
