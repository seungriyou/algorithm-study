# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
p_sum = [0]
for num in nums:
    p_sum.append(p_sum[-1] + num)

for _ in range(M):
    a, b = map(int, input().split())
    print(p_sum[b] - p_sum[a - 1])
