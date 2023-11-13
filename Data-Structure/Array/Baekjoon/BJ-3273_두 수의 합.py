# https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
target = int(input())

d = set()
cnt = 0
for n in nums:
    if n in d:
        cnt += 1
    d.add(target - n)

print(cnt)
