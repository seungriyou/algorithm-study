# https://www.acmicpc.net/problem/2167
import sys; input = sys.stdin.readline

# prefix sum으로도 가능

N, M = map(int, input().split())
dp = [[0] + list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M + 1)] + dp

# dp[i][j]: upper left (1, 1) 부터 (i, j) 까지의 합
# dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]) + dp[i][j]
# -> dp[i - 1][j - 1]은 dp[i - 1][j]과 dp[i][j - 1]에서 중복되므로 빼주어야 함
for r in range(N + 1):
    for c in range(M + 1):
        dp[r][c] += dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    # "(x, y) 까지의 합"에서
    # "(x, j - 1) 까지의 합"과 "(i - 1, y) 까지의 합"을 빼야함
    # 이때, "(i - 1, j - 1) 까지의 합"이 중복으로 빼지므로 한 번 더해야 함
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])
