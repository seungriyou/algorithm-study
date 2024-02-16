# https://www.acmicpc.net/problem/23288
import sys; input = sys.stdin.readline
from collections import deque

# TIP: 방향 shifting (ex. %, xor)

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dice = [1, 2, 3, 4, 5, 6]

# 0, 1, 2, 3 = 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def roll_dice(d):
    """
    dice의 인덱스를 전개도에 나타내면 다음과 같다.

        1
    3   0   2
        4
        5

    d       before      after
    --  --  ---------   ---------
    동   0   3 0 2 5     5 3 0 2
    남   1   1 0 4 5     5 1 0 4
    서   2   3 0 2 5     0 2 5 3
    북   3   1 0 4 5     0 4 5 1
    """

    if d == 0:
        dice[3], dice[0], dice[2], dice[5] = dice[5], dice[3], dice[0], dice[2]

    elif d == 1:
        dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]

    elif d == 2:
        dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]

    elif d == 3:
        dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]


def get_score(x, y):
    b, c = graph[x][y], 1

    q = deque([(x, y)])
    visited = {(x, y)}

    while q:
        x, y = q.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 벗어났거나 이미 방문했다면 넘어가기
            if nx < 0 or nx >= N or ny < 0 or ny >= M or (nx, ny) in visited:
                continue

            # b 값과 같다면 이동하기
            if graph[nx][ny] == b:
                q.append((nx, ny))
                visited.add((nx, ny))
                c += 1

    return b * c


def get_next_d(d, x, y):
    a, b = dice[5], graph[x][y]

    if a > b:
        # 90도 시계 방향 회전
        d = (d + 1) % 4

    elif a < b:
        # 90도 반시계 방향 회전
        d = (d + 3) % 4

    return d


# 초기화
d, x, y, score = 0, 0, 0, 0

for _ in range(K):
    # 1. 주사위가 굴러갈 위치로 x, y 업데이트 (필요 시 d도 업데이트)
    # 이동 방향에 칸이 없다면, 이동 방향을 반대로
    if x + dx[d] < 0 or x + dx[d] >= N or y + dy[d] < 0 or y + dy[d] >= M:
        d ^= 2  # d = (d + 2) % 4
    x, y = x + dx[d], y + dy[d]

    # 2. d 방향으로 주사위 굴리기 (dice 업데이트)
    roll_dice(d)

    # 3. (x, y) 위치에서의 점수 획득
    score += get_score(x, y)

    # 4. 다음 이동 방향 d 결정
    d = get_next_d(d, x, y)

print(score)
