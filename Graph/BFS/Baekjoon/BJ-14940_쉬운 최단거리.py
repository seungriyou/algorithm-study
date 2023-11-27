# https://www.acmicpc.net/problem/14940
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(x, y)])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않고, 아직 방문하지 않았고, 방문 가능한 칸이면
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1     # 거리 기록
                q.append((nx, ny))


start = None
for i in range(N):
    for j in range(M):
        # 방문할 수 있는 칸은 -1로 변경 (graph에 바로 최단거리 기록하기 위해서)
        if graph[i][j] == 1:
            graph[i][j] = -1
        # 시작점을 발견하면 기록
        elif graph[i][j] == 2:
            start = (i, j)

# 시작점에서 출발
bfs(*start)

for row in graph:
    print(*row)
