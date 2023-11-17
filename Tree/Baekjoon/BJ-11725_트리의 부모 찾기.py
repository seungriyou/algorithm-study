# https://www.acmicpc.net/problem/11725
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [-1] * (N + 1) # visited 용도로도 쓰임

q = deque([1])

while q:
    pos = q.popleft()
    for npos in graph[pos]:
        if parent[npos] == -1:
            q.append(npos)
            parent[npos] = pos

for i in range(2, N + 1):
    print(parent[i])
