# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    dp = [0] * 2_000
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1_234_567

    return dp[n]
