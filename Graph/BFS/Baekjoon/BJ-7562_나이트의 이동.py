# https://www.acmicpc.net/problem/7562

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
testcases = []
for _ in range(n):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    testcases.append([l, start, end])

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs(l, start, end):
    graph = [[-1] * l for _ in range(l)]
    q = deque([start])
    graph[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()
        # 종료 조건
        if x == end[0] and y == end[1]:
            return graph[x][y]
        # 방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < l and ny >= 0 and ny < l and graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return

for tc in testcases:
    print(bfs(*tc))
