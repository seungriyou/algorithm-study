# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    """
    Two Pointer
    - 길이가 홀수
    - 길이가 짝수
    """

    n = len(s)
    answer = 0

    # early stop
    if n < 2 or s == s[::-1]:
        return n

    def expand(lo, hi):
        # s[lo] ~ s[hi]에서 양쪽으로 1씩 늘려가며 palindrome 길이 업데이트
        while lo >= 0 and hi < n and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return hi - lo - 1

    # 각 위치에서 (1) 홀수 길이 palindrome (2) 짝수 길이 palindrome 의 길이의 최댓값 찾기
    for i in range(n):
        answer = max(answer, expand(i, i), expand(i, i + 1))

    return answer


def solution2(s):
    """
    2D DP
    dp[lo][hi]: s[lo] ~ s[hi]가 palindrome인지 여부
        - lo == hi: 길이 1인 palindrome 이므로 True
        - lo + 1 == hi: s[lo] == s[hi]
        - 그 외: dp[lo + 1][hi - 1] && s[lo] == s[hi]
                -> lo는 오른쪽 값을 봐야하므로, lo는 오른쪽부터 순회해야 함!
    """

    n = len(s)
    answer = 0

    # early stop
    if n < 2 or s == s[::-1]:
        return n

    dp = [[False] * n for _ in range(n)]

    for lo in range(n - 1, -1, -1):
        for hi in range(lo, n):
            if lo == hi:
                dp[lo][hi] = True
            elif lo + 1 == hi:
                dp[lo][hi] = s[lo] == s[hi]
            else:
                dp[lo][hi] = s[lo] == s[hi] and dp[lo + 1][hi - 1]

            # longest palindrome 길이 업데이트
            if dp[lo][hi] and (new_len := hi - lo + 1) > answer:
                answer = new_len

    return answer
