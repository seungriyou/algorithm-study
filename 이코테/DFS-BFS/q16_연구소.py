# https://www.acmicpc.net/problem/14502

from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
graph = []
# walled_graph = [[0] * m for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def move_virus(walled_graph, r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nc >= 0 and nr < n and nc < m:
            if walled_graph[nr][nc] == 0:
                walled_graph[nr][nc] = 2
                move_virus(walled_graph, nr, nc)

def get_size(final_graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if final_graph[i][j] == 0:
                cnt += 1
    return cnt

# 벽을 설치할 수 있는 영역의 좌표 모으기
safe_zone = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            safe_zone.append((i, j))

result = 0
# 3개의 벽을 설치하는 경우의 수를 구하고 벽을 세운 후, 바이러스를 전파해보고 최댓값 갱신
for a, b, c in combinations(safe_zone, 3):
    walled_graph = deepcopy(graph)
    walled_graph[a[0]][a[1]] = 1
    walled_graph[b[0]][b[1]] = 1
    walled_graph[c[0]][c[1]] = 1
    for i in range(n):
        for j in range(m):
            if walled_graph[i][j] == 2:
                move_virus(walled_graph, i, j)
    result = max(result, get_size(walled_graph))

print(result)
