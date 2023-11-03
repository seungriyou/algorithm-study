# https://www.acmicpc.net/problem/1012
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny]:
            graph[nx][ny] = 0
            dfs(nx, ny)

    # base condition
    # if x < 0 or x >= M or y < 0 or y >= N or not graph[x][y]:
    #     return
    #
    # graph[x][y] = 0
    #
    # dfs(x - 1, y)
    # dfs(x + 1, y)
    # dfs(x, y - 1)
    # dfs(x, y + 1)

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
                dfs(i, j)
                cnt += 1
    print(cnt)
