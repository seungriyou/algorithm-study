# https://www.acmicpc.net/problem/3190
import sys; input = sys.stdin.readline
from collections import deque

N = int(input())

apples = set()
for _ in range(int(input())):
    r, c = map(int, input().split())
    apples.add((r - 1, c - 1))

directions = {}
for _ in range(int(input())):
    n, d = input().split()
    directions[int(n)] = d

# idx: 0, 1, 2, 3 = 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

snake = deque([(0, 0)])     # 맨위 맨좌측에 위치
snake_d = 0                 # 오른쪽을 향함

seconds = 0


def rotate(snake_d, d):
    if d == "L":
        return (snake_d + 3) % 4
    elif d == "D":
        return (snake_d + 1) % 4


while True:
    # 1. 새로운 second 시작 (tick)
    seconds += 1

    # 2. 새로운 머리 위치 구하기
    r, c = snake[-1]                            # 현재 머리 위치
    nr, nc = r + dr[snake_d], c + dc[snake_d]   # 새로운 머리 위치

    # 2-1. (1) 벽이나 (2) 자기자신의 몸과 부딪히면 종료
    if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in snake:
        break
    # 2-2. 아니면 snake에 추가
    snake.append((nr, nc))

    # 3-1. 이동한 칸에 사과가 있다면, 사과 제거
    if (nr, nc) in apples:
        apples.remove((nr, nc))
    # 3-2. 이동한 칸에 사과가 없다면, 꼬리 삭제
    else:
        snake.popleft()

    # 4. 방향을 전환하는 경우에 해당한다면, 방향 전환
    if seconds in directions:
        snake_d = rotate(snake_d, directions[seconds])


print(seconds)
