# [BJ] 1926 - 그림
# https://www.acmicpc.net/problem/1926

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 0
    area = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny]:
                q.append((nx, ny))
                graph[nx][ny] = 0
                area += 1

    return area

# 값이 1인 모든 노드에서 bfs 탐색
# visited 임은 값을 1->0으로 바꿈으로써 표시
cnt = max_area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            max_area = max(max_area, bfs(i, j))
            cnt += 1

print(cnt)
print(max_area)
