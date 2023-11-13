# https://www.acmicpc.net/problem/1158
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(range(1, N + 1))
result = []
prev = 0
while nums:
    prev = (prev - 1 + K) % len(nums)   # prev 위치의 원소를 pop 하므로 -1 한 후 K 칸 점프
    result.append(nums.pop(prev))

print("<" + ", ".join(map(str, result)) + ">")
