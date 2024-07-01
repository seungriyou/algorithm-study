# [PG] 42578 - 의상 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict


def solution(clothes):
    closet = defaultdict(list)
    for n, t in clothes:
        closet[t].append(n)

    answer = 1
    for names in closet.values():
        answer *= len(names) + 1  # -- 해당 종류에서 아무 것도 고르지 않는 경우 추가 (+1)

    return answer - 1  # -- 모든 종류에서 아무 것도 고르지 않는 경우 제거 (-1)


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
assert 5 == solution(clothes)


##### review #####
def solution(clothes):
    cnt = defaultdict(int)

    for _, ctype in clothes:
        cnt[ctype] += 1

    res = 1
    for c in cnt.values():
        res *= (c + 1)

    return res - 1
