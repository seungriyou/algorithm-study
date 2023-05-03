# [BOJ] 2667 - 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, [*input().rstrip()])) for _ in range(n)]

num = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    # 주의: 시작점 방문 처리
    graph[x][y] = 0
    q = deque([(x, y)])
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
           result.append(bfs(graph, i, j))

result.sort()

print(len(result))
for n in result:
    print(n)
