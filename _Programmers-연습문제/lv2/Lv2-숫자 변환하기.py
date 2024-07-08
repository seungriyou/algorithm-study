# https://school.programmers.co.kr/learn/courses/30/lessons/154538

def solution(x, y, n):
    """heap"""
    import heapq

    # y -> x로 거꾸로
    q = [(0, y)]  # [(cnt, val)]

    while q:
        cnt, val = heapq.heappop(q)

        if val == x:
            return cnt

        if val >= n:
            heapq.heappush(q, (cnt + 1, val - n))
        if val % 2 == 0:
            heapq.heappush(q, (cnt + 1, val // 2))
        if val % 3 == 0:
            heapq.heappush(q, (cnt + 1, val // 3))

    return -1


def solution1(x, y, n):
    """DP"""

    INF = 1_000_0001
    dp = [INF] * (y - x + 1)
    dp[0] = 0

    for i in range(1, y - x + 1):
        if i >= n:
            dp[i] = min(dp[i], dp[i - n] + 1)
        if i + x >= 2 * x and (i + x) % 2 == 0:
            dp[i] = min(dp[i], dp[(i + x) // 2 - x] + 1)
        if i + x >= 3 * x and (i + x) % 3 == 0:
            dp[i] = min(dp[i], dp[(i + x) // 3 - x] + 1)

    return -1 if dp[-1] == INF else dp[-1]
