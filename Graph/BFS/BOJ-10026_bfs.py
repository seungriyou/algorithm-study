# [BOJ] 10026 - 적록색약
# https://www.acmicpc.net/problem/10026

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[*input().rstrip()] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

red = 0
green = 0

blue = 0
red_green = 0

# step 마다 visited로 처리할 때 사용할 값
VISITED = {
    1: "M",
    2: 0
}

def bfs(x, y, c, step):
    # 주의: 시작점도 방문한 것으로 처리
    graph[x][y] = VISITED[step]
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 방문하지 않았고 출발 지점과 색깔이 동일한 경우
            if graph[nx][ny] == c:
                graph[nx][ny] = VISITED[step]
                q.append((nx, ny))

    return True

# (1) R과 G 영역의 개수를 세고, M으로 바꿔준다. (같은 숫자로 만들어서 하나의 영역으로)
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            if bfs(i, j, "R", 1):
                red += 1
        elif graph[i][j] == "G":
            if bfs(i, j, "G", 1):
                green += 1

# (2) R과 G 영역이 합쳐졌으므로, 다시 bfs를 수행한다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == "B":
            if bfs(i, j, "B", 2):
                blue += 1
        elif graph[i][j] == "M":
            if bfs(i, j, "M", 2):
                red_green += 1

print(red + green + blue, red_green + blue)