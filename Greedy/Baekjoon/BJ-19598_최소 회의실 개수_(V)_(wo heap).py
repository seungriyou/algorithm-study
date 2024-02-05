# https://www.acmicpc.net/problem/19598
import sys; input = sys.stdin.readline
N = int(input())

# heapq 없이도 풀 수 있다!

start = []
end = []
for _ in range(N):
    s, e = map(int, input().split())
    start.append(s)
    end.append(e)

start.sort()
end.sort()

i = 0
cnt = N

for s in start:
    if end[i] <= s:
        # 하나의 회의실에서 이어서 가능함
        cnt -= 1
        i += 1

print(cnt)
