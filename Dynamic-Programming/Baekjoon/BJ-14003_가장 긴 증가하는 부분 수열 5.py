# https://www.acmicpc.net/problem/14003
import sys
import bisect
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# memo[i] = 길이가 (i + 1)인 LIS의 맨 마지막 원소가 될 수 있는 값 중 가장 작은 값
memo = [nums[0]]
# dp[i] = nums[i]가 포함된 LIS의 길이
dp = [1]

for i in range(1, N):
    if memo[-1] < nums[i]:
        memo.append(nums[i])
        dp.append(len(memo))
    else:
        idx = bisect.bisect_left(memo, nums[i])
        memo[idx] = nums[i]
        dp.append(idx + 1)

max_length = len(memo)  # == max(dp)
max_idx = dp.index(max_length)    # input 크기가 크므로 index() 오래 걸릴 수도 있지 않을까..?
print(max_length)

# 가장 긴 LIS의 마지막 원소로부터 역추적
lis = []
# for i in range(N - 1, -1, -1):      # if w/o max_idx
for i in range(max_idx, -1, -1):  # if w/ max_idx
    if dp[i] == max_length:
        lis.append(nums[i])
        max_length -= 1
    if max_length == 0:
        break
# while max_idx >= 0 or max_length > 0:
#     if dp[max_idx] == max_length:
#         lis.append(nums[max_idx])
#         max_length -= 1
#     max_idx -= 1
lis.reverse()
print(*lis)
