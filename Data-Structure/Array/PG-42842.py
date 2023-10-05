# [PG] 42842 - 카펫 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

import math


def solution2(brown, yellow):
    total = brown + yellow

    w = math.ceil(math.sqrt(total))

    while w < total:
        h = total // w
        if w * h == total and (w - 2) * (h - 2) == yellow:
            return [w, h]
        w += 1


def solution(brown, yellow):
    # 가능한 yellow 부분의 height = 1 ~ int(sqrt(yellow))
    for h in range(1, int(yellow ** 0.5) + 1):
        if yellow % h == 0 and brown == 2 * (yellow // h + h) + 4:
            return [yellow // h + 2, h + 2]


brown = 24
yellow = 24
assert [8, 6] == solution(brown, yellow) == solution2(brown, yellow)
