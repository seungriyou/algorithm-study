# [BJ] 7576 - 토마토
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

def min_day(tomato, graph):
    # 이미 모든 토마토가 익어있다면 0 출력
    if len(tomato) == m * n:
        return 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque(tomato)
    day = 0

    # BFS 수행
    while q:
        x, y, d = q.popleft()
        day = d

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx, ny, d + 1))
                elif graph[nx][ny] == -1:
                    continue

    # 토마토가 모두 익지 못하는 상황이면 -1 출력
    for g in graph:
        if 0 in g:
            return -1

    return day

print(min_day(tomato, graph))
