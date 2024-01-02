# https://www.acmicpc.net/problem/20055
# TIP: deque.rotate()

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(map(int, input().split()))  # durability


def solution(N: int, K: int, belt: deque) -> int:
    step = 0
    robot = deque([False] * N)

    # K: 하나씩 줄여나가면서 0이 되면 종료
    while K > 0:
        step += 1

        # 1. belt와 robot이 함께 회전
        belt.rotate(1)
        robot.rotate(1)

        # 내리는 위치(= N번 칸)에 도달한 robot은 그 즉시 내림
        robot[N - 1] = False

        # 2. belt의 오른쪽에 위치한 robot부터, belt 회전 방향으로 한 칸 이동할 수 있는지 여부를 검사 후 이동
        for i in range(N - 2, -1, -1):
            # 조건: (1) 이동하려는 칸에 로봇이 없으며 (2) 그 칸의 내구도가 1 이상
            if robot[i] and not robot[i + 1] and belt[i + 1] > 0:
                robot[i], robot[i + 1] = False, True
                belt[i + 1] -= 1

                # 그 칸의 내구도가 0에 도달하면 K--
                K -= (belt[i + 1] == 0)

        # 내리는 위치(= N번 칸)에 도달한 robot은 그 즉시 내림
        robot[N - 1] = False

        # 3. 올리는 위치(= 1번 칸)의 내구도가 0이 아니면 robot 올리기
        if belt[0] > 0:
            robot[0] = True
            belt[0] -= 1

            # 그 칸의 내구도가 0에 도달하면 K--
            K -= (belt[0] == 0)

    return step


print(solution(N, K, belt))
