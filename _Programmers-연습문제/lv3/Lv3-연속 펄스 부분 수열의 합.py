# https://school.programmers.co.kr/learn/courses/30/lessons/161988

def solution(sequence):
    """prefix sum"""

    ps = [0]

    for i, seq in enumerate(sequence):
        """홀/짝마다 펄스의 부호를 바꿔가며 누적합 구하기"""
        if i & 1:
            ps.append(ps[-1] - seq)
        else:
            ps.append(ps[-1] + seq)

    # 가장 큰 구간 반환
    return max(ps) - min(ps)


def solution1(sequence):
    """1D DP"""

    n = len(sequence)
    answer = 0
    a, b = 0, 0

    for i in range(1, n + 1):
        seq = sequence[i - 1]

        # dp[i][0] : 현재 보고 있는 sequence[i - 1]에 -1을 곱하는 경우
        ca = max(b - seq, -seq)

        # dp[i][1] : 현재 보고 있는 sequence[i - 1]에 1을 곱하는 경우
        cb = max(a + seq, seq)

        # answer 업데이트
        answer = max(answer, ca, cb)

        # a, b 업데이트
        a, b = ca, cb

    return answer


def solution2(sequence):
    """2D DP"""

    n = len(sequence)
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]
    answer = 0

    for i in range(1, n + 1):
        seq = sequence[i - 1]

        # dp[i][0] : 현재 보고 있는 sequence[i - 1]에 -1을 곱하는 경우
        dp[i][0] = max(dp[i - 1][1] - seq, -seq)

        # dp[i][1] : 현재 보고 있는 sequence[i - 1]에 1을 곱하는 경우
        dp[i][1] = max(dp[i - 1][0] + seq, seq)

        answer = max(answer, max(dp[i]))

    return answer
