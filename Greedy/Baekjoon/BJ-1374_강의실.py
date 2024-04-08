# https://www.acmicpc.net/problem/1374
import sys; input = sys.stdin.readline
import heapq

N = int(input())

# lecture 시작하는 시각 - 끝나는 시각 우선순위로 오름차순 정렬
lectures = sorted([tuple(map(int, input().split()))[1:] for _ in range(N)])
# lecture 끝나는 시각 모으기
q = []

for lecture in lectures:
    s, e = lecture

    if q and q[0] <= s:
        heapq.heappop(q)
    heapq.heappush(q, e)

print(len(q))

