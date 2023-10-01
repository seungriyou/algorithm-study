# [PG] 42576 - 완주하지 못한 선수 (Lv1)
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import defaultdict, Counter


def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]


def solution2(participant, completion):
    cnt = defaultdict(int)

    for p in participant:
        cnt[p] += 1
    for c in completion:
        cnt[c] -= 1

    for name, i in cnt.items():
        if i == 1:
            return name


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
assert "vinko" == solution(participant, completion)
assert "vinko" == solution2(participant, completion)
