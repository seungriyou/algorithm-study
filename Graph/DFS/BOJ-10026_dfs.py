# [BOJ] 10026 - 적록색약
# https://www.acmicpc.net/problem/10026

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[*input().rstrip()] for _ in range(n)]

red = 0
green = 0
red_green = 0
blue = 0

VISITED = {
    1: "RG",
    2: 0
}

def dfs(graph, x, y, c, step):
    # 범위 검사
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if graph[x][y] == c:
        graph[x][y] = VISITED[step]
        dfs(graph, x - 1, y, c, step)
        dfs(graph, x + 1, y, c, step)
        dfs(graph, x, y - 1, c, step)
        dfs(graph, x, y + 1, c, step)

    return

# [step 1] R, G만 각각 세고, 같은 색깔로 칠하기
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            dfs(graph, i, j, "R", 1)
            red += 1
        elif graph[i][j] == "G":
            dfs(graph, i, j, "G", 1)
            green += 1
        else:
            continue

# [step 2] RG, B를 각각 세고, 방문한 곳은 0으로 칠하기
for i in range(n):
    for j in range(n):
        if graph[i][j] == "RG":
            dfs(graph, i, j, "RG", 2)
            red_green += 1
        elif graph[i][j] == "B":
            dfs(graph, i, j, "B", 2)
            blue += 1
        else:
            continue

# 결과 출력
print(red + green + blue, red_green + blue)
