# [PG] 42840 - 모의고사 (Lv1)
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

from itertools import cycle


def solution(answers):
    patterns = [
        cycle([1, 2, 3, 4, 5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]),
    ]
    scores = [0] * 3

    for a in answers:
        for i in range(3):
            if next(patterns[i]) == a:
                scores[i] += 1

    return [i + 1 for i, s in enumerate(scores) if s == max(scores)]


def solution2(answers):
    n_1 = [1, 2, 3, 4, 5]
    n_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0] * 3

    for i, a in enumerate(answers):
        if a == n_1[i % len(n_1)]:
            scores[0] += 1
        if a == n_2[i % len(n_2)]:
            scores[1] += 1
        if a == n_3[i % len(n_3)]:
            scores[2] += 1

    return [i + 1 for i, s in enumerate(scores) if s == max(scores)]


answers = [1,3,2,4,2]
assert [1, 2, 3] == solution(answers)
assert [1, 2, 3] == solution2(answers)
