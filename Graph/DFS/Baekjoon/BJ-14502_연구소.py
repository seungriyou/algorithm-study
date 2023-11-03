# https://www.acmicpc.net/problem/14502
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
empty = []
viruses = []
answer = 0
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 0:
            empty.append((i, j))
        elif graph[i][j] == 2:
            viruses.append((i, j))

# def count_area(graph):
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             cnt += graph[i][j] == 0
#     return cnt

def backtrack(depth, idx):
    global answer

    # base condition
    if depth == 3:
        copied_graph = [row[:] for row in graph]
        # dfs
        for vi, vj in viruses:
            move_virus(copied_graph, vi, vj)
        # 영역 세기
        cnt = sum(row.count(0) for row in copied_graph)
        # 업데이트
        answer = max(answer, cnt)
        # answer = max(answer, count_area(copied_graph))
        return

    # recur
    for i in range(idx, len(empty)):
        x, y = empty[i]
        graph[x][y] = 1
        backtrack(depth + 1, i + 1)
        graph[x][y] = 0


def move_virus(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            move_virus(graph, nx, ny)


backtrack(0, 0)
print(answer)
