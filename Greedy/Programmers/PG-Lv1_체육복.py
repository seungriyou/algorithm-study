# [PG] 42862 - 체육복 (Lv1)
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for r in set_reserve:
        if r - 1 in set_lost:  # -- 왼쪽부터 확인
            set_lost.remove(r - 1)
        elif r + 1 in set_lost:
            set_lost.remove(r + 1)

    return n - len(set_lost)


n = 5
lost = [2, 4]
reserve = [1, 3, 5]
assert 5 == solution(n, lost, reserve)
