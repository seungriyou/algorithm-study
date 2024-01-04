# https://www.acmicpc.net/problem/14503
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
R, C, D = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(N)]

# [북, 동, 남, 서]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0


def clean(r: int, c: int, d: int) -> None:
    global cnt

    # 1. 현재 칸이 청소되지 않았다면 청소
    if place[r][c] == 0:
        place[r][c] = 2     # 청소되었음을 표시
        cnt += 1

    # 2. 현재 방향에서 반시계 방향으로 90도씩 회전하면서
    for _ in range(4):
        d = (d + 3) % 4     # ex. 2 -> 1 -> 0 -> 3 (반시계)
        nr, nc = r + dr[d], c + dc[d]

        # 2-1. 청소되지 않은 빈 칸을 발견한 경우
        # 진행 가능 조건: 전진 시의 좌표가 범위를 벗어나지 않으며, 청소되지 않은 칸인지 확인
        if 0 <= nr < N and 0 <= nc < M and place[nr][nc] == 0:
            return clean(nr, nc, d)

    # 2-2. 청소되지 않은 빈 칸이 없는 경우
    nr, nc = r - dr[d], c - dc[d]
    # 후진 가능 조건: 후진 시의 좌표가 범위를 벗어나지 않으며, 벽이 아닌지 확인
    if 0 <= nr < N and 0 <= nc < M and place[nr][nc] != 1:
        return clean(nr, nc, d)


clean(R, C, D)
print(cnt)
