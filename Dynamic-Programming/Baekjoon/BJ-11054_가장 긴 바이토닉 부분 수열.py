# https://www.acmicpc.net/problem/11054
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# dp를 두 번 진행 (증가 / 감소)
dp1 = [1] * N
dp2 = [1] * N

# dp1 (증가)
for i in range(N):
    for j in range(i):
        # if nums[j] < nums[i]:
        #     dp1[i] = max(dp1[i], dp1[j] + 1)
        if nums[j] < nums[i] and dp1[i] < dp1[j] + 1:
            dp1[i] = dp1[j] + 1

# dp2 (감소)
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        # if nums[j] < nums[i]:
        #     dp2[i] = max(dp2[i], dp2[j] + 1)
        if nums[j] < nums[i] and dp2[i] < dp2[j] + 1:
            dp2[i] = dp2[j] + 1
# nums.reverse()
# for i in range(N):
#     for j in range(i):
#         # if nums[j] < nums[i]:
#         #     dp2[i] = max(dp2[i], dp2[j] + 1)
#         if nums[j] < nums[i] and dp2[i] < dp2[j] + 1:
#             dp2[i] = dp2[j] + 1
# dp2.reverse()

max_length = 0
for u, d in zip(dp1, dp2):
    max_length = max(max_length, u + d)

print(max_length - 1)
