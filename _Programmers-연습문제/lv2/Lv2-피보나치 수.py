# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, (a + b) % 1_234_567

    return a


def solution1(n):
    prev1, prev2 = 1, 0

    for _ in range(2, n + 1):
        curr = (prev2 + prev1) % 1_234_567
        prev2, prev1 = prev1, curr

    return prev1


def solution2(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1_234_567

    return dp[n]
