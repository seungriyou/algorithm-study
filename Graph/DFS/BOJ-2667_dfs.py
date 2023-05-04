# [BOJ] 2667 - 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline

n = int(input())
graph = [[*map(int, input().rstrip())] for _ in range(n)]


def dfs(graph, x, y):
    # 범위 검사
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    global cnt_houses
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt_houses += 1

        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x, y + 1)

    return

cnt = 0
cnt_houses_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            cnt_houses = 0
            dfs(graph, i, j)
            cnt_houses_list.append(cnt_houses)
            cnt += 1
cnt_houses_list.sort()

print(cnt)
for c in cnt_houses_list:
    print(c)
