# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    # prev2 == dp[i - 2], prev1 == dp[i - 1]
    prev2 = prev1 = 1  # == dp[1]

    for _ in range(1, n):
        curr = (prev2 + prev1) % 1_000_000_007
        prev2, prev1 = prev1, curr

    return prev1
