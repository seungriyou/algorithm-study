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

# LIS의 맨 마지막 원소부터 lis 채워나가기
lis = []
while max_idx >= 0: # or max_length > 0:
    if dp[max_idx] == max_length:
        lis.append(nums[max_idx])
        max_length -= 1
    max_idx -= 1
lis.reverse()
print(*lis)
