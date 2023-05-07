# [BOJ] 1260 - DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        next_n = q.popleft()
        print(next_n, end=" ")
        for i in graph[next_n]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

n, m, v = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)
