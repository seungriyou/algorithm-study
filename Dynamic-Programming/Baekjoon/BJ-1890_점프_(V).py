# https://www.acmicpc.net/problem/1890
import sys; input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        # [주의]
        # 1. dp[r][c] == 0이면 경로에 포함되지 않으므로 continue
        # 2. board[N - 1][N - 1]을 볼 때는 그냥 넘어가야 함 (d = 0이 되므로 값이 중복해서 더해지게 됨)
        if not dp[r][c] or (r == N - 1 and c == N - 1):
            continue

        d = board[r][c]

        # 오른쪽
        if (nc := c + d) < N:
            dp[r][nc] += dp[r][c]

        # 아래쪽
        if (nr := r + d) < N:
            dp[nr][c] += dp[r][c]

print(dp[N - 1][N - 1])
