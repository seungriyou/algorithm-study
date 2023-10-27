# [BOJ] 11724 - 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1
print(cnt)
