# https://www.acmicpc.net/problem/2583

from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[m - 1 - i][j] = 1     # 직사각형 영역 -> 벽 세우기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 1
    area = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny))
                area += 1

    return area

areas = []
cnt = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            areas.append(bfs(i, j))
            cnt += 1

areas.sort()
print(cnt)
print(' '.join(map(str, areas)))
