# https://www.acmicpc.net/problem/2630
import sys; input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

cnt = [0, 0] # (white, blue)

def check_color(r, c, length):
    # 1: blue, 0: white, -1: different
    color = paper[r][c]

    for i in range(r, r + length):
        for j in range(c, c + length):
            if color != paper[i][j]:
                return -1

    return color

def solve(r, c, length):
    color = check_color(r, c, length)

    # 전체 color가 같지 않은 경우 -> 색종이를 나눠야 함
    if color == -1:
        mid = length // 2
        solve(r, c, mid)
        solve(r + mid, c, mid)
        solve(r, c + mid, mid)
        solve(r + mid, c + mid, mid)

    # 전체 color가 blue인 경우
    elif color == 1:
        cnt[1] += 1

    # 전체 color가 white인 경우
    elif color == 0:
        cnt[0] += 1

solve(0, 0, N)

print(cnt[0])
print(cnt[1])
