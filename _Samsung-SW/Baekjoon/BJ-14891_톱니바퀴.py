# https://www.acmicpc.net/problem/14891
import sys
from collections import deque
input = sys.stdin.readline


def get_score(gears: list[deque]) -> int:
    score = 0

    if gears[0][0] == 1:
        score += 1
    if gears[1][0] == 1:
        score += 2
    if gears[2][0] == 1:
        score += 4
    if gears[3][0] == 1:
        score += 8

    return score


def spin_left(idx: int, direction: int) -> None:
    # 종료 조건
    if idx < 0:
        return
    # 맞물리는 톱니의 극이 다르다면
    if gears[idx][2] != gears[idx + 1][6]:
        # 왼쪽 톱니바퀴도 살펴보기
        spin_left(idx - 1, -direction)
        # 현재 톱니바퀴 회전
        gears[idx].rotate(direction)


def spin_right(idx: int, direction: int) -> None:
    # 종료 조건
    if idx > 3:
        return
    # 맞물리는 톱니의 극이 다르다면
    if gears[idx - 1][2] != gears[idx][6]:
        # 오른쪽 톱니바퀴도 살펴보기
        spin_right(idx + 1, -direction)
        # 현재 톱니바퀴 회전
        gears[idx].rotate(direction)


gears = [deque(map(int, input().rstrip())) for _ in range(4)]
for _ in range(int(input())):
    spin_idx, direction = map(int, input().split())
    spin_idx -= 1
    # 왼쪽 톱니바퀴 회전
    spin_left(spin_idx - 1, -direction)
    # 오른쪽 톱니바퀴 회전
    spin_right(spin_idx + 1, -direction)
    # 현재 톱니바퀴 회전
    gears[spin_idx].rotate(direction)


print(get_score(gears))
