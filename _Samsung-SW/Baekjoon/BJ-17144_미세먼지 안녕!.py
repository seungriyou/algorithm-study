# https://www.acmicpc.net/problem/17144
import sys; input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]


# === 함수 === #
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 미세먼지 확산 함수
def spread():
    # 1. 미세먼지의 좌표 & 미세먼지 양 얻기
    dusts = []      # (r, c, 미세먼지 양)
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                dusts.append((i, j, graph[i][j]))

    # 2. 모든 미세먼지 좌표에서 확산 & 남은 미세먼지 양 계산
    for x, y, d in dusts:
        # 주변으로 확산될 양
        spread_amount = int(d / 5)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # (1) 칸이 없거나 (2) 인접한 방향에 공기청정기가 있으면 넘어가기
            if nx < 0 or nx >= R or ny < 0 or ny >= C or graph[nx][ny] == -1:
                continue

            # 확산
            graph[nx][ny] += spread_amount
            # 남은 양 계산
            graph[x][y] -= spread_amount


# 공기청정기 함수
def clean(x1, x2):
    # 1. 위쪽
    for i in range(x1 - 2, -1, -1):
        graph[i + 1][0] = graph[i][0]
    for j in range(1, C):
        graph[0][j - 1] = graph[0][j]
    for i in range(1, x1 + 1):
        graph[i - 1][C - 1] = graph[i][C - 1]
    for j in range(C - 2, 0, -1):
        graph[x1][j + 1] = graph[x1][j]
    graph[x1][1] = 0

    # 2. 아래쪽
    for i in range(x2 + 2, R):
        graph[i - 1][0] = graph[i][0]
    for j in range(1, C):
        graph[R - 1][j - 1] = graph[R - 1][j]
    for i in range(R - 1, x2 - 1, -1):
        graph[i][C - 1] = graph[i - 1][C - 1]
    for j in range(C - 2, 0, -1):
        graph[x2][j + 1] = graph[x2][j]
    graph[x2][1] = 0


# 미세먼지 양 계산 함수
def get_dust_amount():
    amount = 0
    for i in range(R):
        for j in range(C):
            if graph[i][j] != -1:
                amount += graph[i][j]

    return amount


def solution():
    # 공기청정기 좌표 구하기
    cleaner = []
    for i in range(R):
        if graph[i][0] == -1:
            cleaner += [i, i + 1]
            break

    # T초 동안 미세먼지 계산
    for _ in range(T):
        # 1. 미세먼지 확산
        spread()

        # 2. 공기청정기
        clean(*cleaner)

    # 방에 남아있는 미세먼지 양 출력
    print(get_dust_amount())


solution()
