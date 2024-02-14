# https://www.acmicpc.net/problem/14499
import sys; input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))

dice = [0] * 6

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def roll_dice(d):
    """
    dice = [0, 0, 0, 0, 0, 0] 일때, index를 전개도에 나타내면 다음과 같다.
    이때, dice[0] = 윗면, dice[2] = 동쪽이다.

        1
     3  0  2
        4
        5

    d   d   before      after
    --  --  ----------  ----------
    1   동   3 0 2 5     5 3 0 2
    2   서   3 0 2 5     0 2 5 3
    3   북   1 0 4 5     0 4 5 1
    4   남   1 0 4 5     5 1 0 4
    """

    if d == 1:
        dice[3], dice[0], dice[2], dice[5] = dice[5], dice[3], dice[0], dice[2]

    elif d == 2:
        dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]

    elif d == 3:
        dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]

    elif d == 4:
        dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]


def update_number(x, y):
    if graph[x][y] == 0:
        # 주사위의 바닥면에 쓰여있는 수가 칸에 복사된다.
        graph[x][y] = dice[5]
    else:
        # 칸에 쓰여있는 수가 주사위의 바닥면으로 복사되고, 칸에 쓰여있는 수는 0이 된다.
        dice[5], graph[x][y] = graph[x][y], 0


for d in directions:
    # 1. 범위 확인 후, 지도에서 벗어났다면 넘어가기
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    x, y = nx, ny

    # 2. 주사위 굴리기
    roll_dice(d)

    # 3. 주사위의 바닥면 or 칸에 쓰여있는 수 업데이트 하기
    update_number(x, y)

    # 4. 주사위의 윗면에 적힌 수 출력하기
    print(dice[0])
