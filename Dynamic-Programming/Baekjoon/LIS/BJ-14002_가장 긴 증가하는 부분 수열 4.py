# https://www.acmicpc.net/problem/14002
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# max_length = dp의 최댓값 = LIS의 길이
# max_idx = 최대 길이의 LIS의 맨 마지막 원소의 index

# max_length = max(dp)
# max_idx = dp.index(max_length)
max_idx = max_length = 0
for i, d in enumerate(dp):
    if d > max_length:
        max_idx = i
        max_length = d
print(max_length)

# 가장 긴 LIS의 마지막 원소로부터 역추적
lis = []
# for i in range(N - 1, -1, -1):    # if w/o max_idx
# for i in range(max_idx, -1, -1):
#     if dp[i] == max_length:
#         lis.append(nums[i])
#         max_length -= 1
#     if max_length == 0:
#         break
while max_idx >= 0 or max_length > 0:
    if dp[max_idx] == max_length:
        lis.append(nums[max_idx])
        max_length -= 1
    max_idx -= 1
lis.reverse()
print(*lis)
