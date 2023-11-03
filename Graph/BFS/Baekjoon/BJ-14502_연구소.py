# https://www.acmicpc.net/problem/14502
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
empty = []
viruses = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty.append((i, j))
        elif graph[i][j] == 2:
            viruses.append((i, j))


def move_virus(graph, r, c):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(r, c)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))


# def count_area(graph):
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             cnt += graph[i][j] == 0
#     return cnt


max_area = 0
for walls in combinations(empty, 3):
    walled_graph = [row[:] for row in graph]
    # 벽 세우기
    for wr, wc in walls:
        walled_graph[wr][wc] = 1
    # 모든 바이러스를 전파
    for vr, vc in viruses:
        move_virus(walled_graph, vr, vc)
    # 안전 영역 크기 최댓값 업데이트
    # max_area = max(max_area, count_area(walled_graph))
    cnt = sum(row.count(0) for row in walled_graph)
    max_area = max(max_area, cnt)

print(max_area)
