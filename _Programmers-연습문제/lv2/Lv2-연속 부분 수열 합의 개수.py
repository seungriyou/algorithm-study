# https://school.programmers.co.kr/learn/courses/30/lessons/131701


def solution(elements):
    n = len(elements)
    vals = set()

    """부분 수열의 <길이>가 아닌 <시작 인덱스>를 기준으로!"""

    # i = 부분 수열 시작 인덱스
    for i in range(n):
        _sum = 0

        # j = 부분 수열 마지막 인덱스
        for j in range(i, i + n):
            _sum += elements[j % n]
            vals.add(_sum)

    return len(vals)
