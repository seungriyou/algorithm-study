# [BJ] 12865 - 평범한 배낭
# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
weights = [0]
values = [0]
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):      # -- 물건 별
    for c in range(k + 1):  # -- (임시) 배낭 용량 별
        # 물건 i의 무게 > 배낭의 용량 c: 해당 물건을 넣을 수 없다.
        if weights[i] > c:
            dp[i][c] = dp[i - 1][c]
        # 물건 i의 무게 <= 배낭의 용량 c: 해당 물건을 배낭에 넣을 수도, 넣지 않을 수도 있다.
        else:
            # max(물건을 배낭에 넣지 않는 경우, 물건을 배낭에 넣는 경우)
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - weights[i]] + values[i])

print(dp[n][k])
