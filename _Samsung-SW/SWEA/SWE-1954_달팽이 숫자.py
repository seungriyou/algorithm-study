# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def snail(N):
    grid = [[0] * N for _ in range(N)]

    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    r, c, d = 0, 0, 0
    grid[0][0] = 1

    for val in range(1, N * N):
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or grid[nr][nc]:
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]

        grid[nr][nc] = val + 1
        r, c = nr, nc

    return grid

if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        print(f"#{test_case}")

        N = int(input())
        grid = snail(N)

        for row in grid:
            print(*row)
