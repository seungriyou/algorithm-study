# https://www.acmicpc.net/problem/15685
import sys
input = sys.stdin.readline

N = int(input())
curves = [list(map(int, input().split())) for _ in range(N)]

"""
세대      방향
-----   -------------------
0세대     0
1세대     0 / 1
2세대     0 1 / 2 1
3세대     0 1 2 1 / 2 3 2 1

정리하면 각 세대에서는, 
    1. 이전 세대 결과의 뒤에서부터
    2. 반시계 방향으로 90도 회전 -> (d + 1) % 4

좌표 -> 좌측하단이 (0, 0)임에 주의
"""

board = [[False] * 101 for _ in range(101)]

# 0: →, 1: ↑, 2: ←, 3: ↓
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 드래곤 커브를 board에 나타내기
for x, y, d, g in curves:
    # 시작 위치 표시
    board[y][x] = True
    directions = [d]

    # g세대까지의 방향 기록
    for _ in range(g):
        # 기존 directions의 뒤에서부터 확인하면서, 반시계 방향으로 90도 회전하여 append
        for i in range(len(directions) - 1, -1, -1):
            directions.append((directions[i] + 1) % 4)

    # 기록한 방향대로 이동하면서 board에 기록
    for i in directions:
        # 방향 따라 움직인 좌표
        x, y = x + dx[i], y + dy[i]
        # 범위를 벗어나지 않았따면 board에 표시
        if 0 <= x <= 100 and 0 <= y <= 100:
            board[y][x] = True

# 네 꼭짓점이 모두 드래곤 커브의 일부인 것 카운트
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            cnt += 1

print(cnt)
