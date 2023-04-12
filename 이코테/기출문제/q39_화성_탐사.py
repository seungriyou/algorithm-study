"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

test_case = []
for _ in range(int(input())):
    n = int(input())
    tc = []
    for _ in range(n):
        tc.append(list(map(int, input().split())))
    test_case.append(tc)

for graph in test_case:
    n = len(graph)
    distance = [[INF] * n for _ in range(n)]

    # 시작 위치
    x, y = 0, 0
    q = [(graph[x][y], x, y)] # (해당 노드로 가기 위한 바용, x좌표, y좌표)
    distance[x][y] = graph[x][y]

    # 다익스트라
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        # 인접한 노드 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어나는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 확인
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n - 1][n - 1])
