# [PG] 42587 - 프로세스 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque


def solution(priorities, location):
    sorted_p = sorted(priorities, reverse=True)  # priorities를 내림차순 정렬한 후, 포인터 p를 이용하여 높은 우선순위 순서대로 비교
    p = 0
    q = deque([(l, i) for i, l in enumerate(priorities)])

    while q and p < len(priorities):
        curr = q.popleft()  # curr = (우선순위, 위치)

        if curr[0] == sorted_p[p]:
            p += 1
            if location == curr[1]:
                return p
        else:
            q.append(curr)


priorities = [1, 1, 9, 1, 1, 1]
location = 0
assert 5 == solution(priorities, location)
