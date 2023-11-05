# https://www.acmicpc.net/problem/16493
import sys
input = sys.stdin.readline

# 배낭의 용량 = 일 수
# 물건 = 챕터
# 가치 = 페이지 수

N, M = map(int, input().split())    # N: 일 수, M: 챕터의 수
days = [0]
pages = [0]
for _ in range(M):
    d, p = map(int, input().split())
    days.append(d)
    pages.append(p)

# dp[i][j]: 임시 일 수 j에서 i 챕터까지 판단했을 때, 최대 페이지 수
dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(M + 1):      # 물건 (챕터)
    for j in range(N + 1):  # 임시 용량 (일 수)
        if days[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - days[i]] + pages[i])

print(dp[M][N])
