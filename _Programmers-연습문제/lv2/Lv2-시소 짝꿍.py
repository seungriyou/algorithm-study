# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import Counter


def solution(weights):
    """조합 경우의 수를 모두 따져서 확인하면 TLE -> Counter 사용"""

    answer = 0
    cnts = Counter(weights)
    combs = {(2, 3), (2, 4), (3, 4)}

    for w in cnts:
        # (1) 같은 weight 끼리의 조합
        answer += cnts[w] * (cnts[w] - 1) // 2
        # (2) {(2, 3), (2, 4), (3, 4)} 비율이 맞는 순열
        for a, b in combs:
            answer += cnts[w] * cnts[w / a * b]

    return answer
