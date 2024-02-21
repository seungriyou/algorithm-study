# [PG] 86491 - 최소직사각형 (Lv1)
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    return max(max(s) for s in sizes) * max(min(s) for s in sizes)

def solution2(sizes):
    max_l = max_s = 0
    for w, h in sizes:
        if w > h:
            max_l = max(max_l, w)
            max_s = max(max_s, h)
        else:
            max_l = max(max_l, h)
            max_s = max(max_s, w)
    return max_l * max_s


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
assert 4000 == solution(sizes)
assert 4000 == solution2(sizes)
