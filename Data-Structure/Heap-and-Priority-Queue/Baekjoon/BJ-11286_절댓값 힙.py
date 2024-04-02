# https://www.acmicpc.net/problem/11286
import sys
import heapq
input = sys.stdin.readline

N = int(input())

q = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(num), num))
