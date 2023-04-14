
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
viruses = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # (virus 종류, 시간, x, y)
            viruses.append((graph[i][j], 0, i, j))

target_s, target_x, target_y = map(int, input().split())

viruses.sort() # 작은 값의 바이러스가 앞에 오도록
q = deque(viruses)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x, y = q.popleft()

    # S초가 지나면 stop
    if s == target_s:
        break
    # 상하좌우
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 검사
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 다음 칸이 비어있다면
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
