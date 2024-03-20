# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    puddles = [(n, m) for m, n in puddles]

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 집 위치에 초기화

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 집 위치면 넘어가기
            if i == 1 and j == 1:
                continue

            # puddle에 해당하면 0으로
            elif (i, j) in puddles:
                dp[i][j] = 0

            # 최단경로 개수는, 윗 칸과 왼쪽 칸까지의 경로의 개수의 합
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1_000_000_007

    return dp[n][m]
