# https://www.acmicpc.net/problem/2644
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]
dist = [-1] * (N + 1)
for _ in range(M):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

q = deque([a])
dist[a] = 0

while q:
    pos = q.popleft()
    for npos in graph[pos]:
        if dist[npos] == -1:
            dist[npos] = dist[pos] + 1
            q.append(npos)

print(dist[b])
