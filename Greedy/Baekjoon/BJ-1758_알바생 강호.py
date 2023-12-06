# https://www.acmicpc.net/problem/1758
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort(reverse=True)

result = 0
for i, n in enumerate(nums):
    if (tip := n - i) > 0:
        result += tip

print(result)
