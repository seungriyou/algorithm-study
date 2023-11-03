# https://www.acmicpc.net/problem/1012
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph[start_x][start_y] = 0
    q = deque([(start_x, start_y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)
