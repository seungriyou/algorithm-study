# https://www.acmicpc.net/problem/1389
import sys
from collections import deque
input = sys.stdin.readline

"""
# 플로이드 워셜 (모든 노드 -> 모든 노드 최단 거리)
N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로 가는 거리는 0으로 초기화
for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_k = INF
min_user = 0
for i in range(1, N + 1):
    if (new_min_k := sum(graph[i][1:])) < min_k:
        min_k = new_min_k
        min_user = i
print(min_user)
"""

# BFS -> 모든 노드에서
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    dist = [-1] * (N + 1)
    q = deque([start])
    dist[0] = dist[start] = 0

    while q:
        pos = q.popleft()
        for npos in graph[pos]:
            if dist[npos] == -1:
                dist[npos] = dist[pos] + 1
                q.append(npos)

    return sum(dist)

min_k = 1_001
min_user = 0
for i in range(1, N + 1):
    k = bfs(i)
    if k < min_k:
        min_k = k
        min_user = i
print(min_user)
