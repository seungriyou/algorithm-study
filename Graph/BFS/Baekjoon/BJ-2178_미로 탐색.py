# [BOJ] 2178 - 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, [*input().rstrip()])))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

bfs(graph, 0, 0)
print(graph[n - 1][m - 1])
