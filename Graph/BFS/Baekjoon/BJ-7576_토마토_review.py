# [BOJ] 7576 - 토마토
# https://www.acmicpc.net/problem/7576

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
tomato = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    tomato.extend([(i, j, 0) for j, r in enumerate(row) if r == 1])

def bfs(graph, tomato):
    day = 0

    # 시간을 크게 줄여준다!
    if len(tomato) == m * n:
        return day

    q = deque(tomato)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, d = q.popleft()
        day = d # max 연산으로 비교할 필요 X

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == -1:
                    continue
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx, ny, day + 1))

    for row in graph:
        if 0 in row:
            day = -1
            break

    return day

print(bfs(graph, tomato))
