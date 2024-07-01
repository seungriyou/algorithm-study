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


##### review #####
def solution(priorities, location):
    sorted_priorities = deque(sorted(priorities, reverse=True))
    ps = deque(enumerate(priorities))

    res = 0

    while ps and sorted_priorities:
        if sorted_priorities[0] == ps[0][1]:
            res += 1
            if ps[0][0] == location:
                return res

            sorted_priorities.popleft()
            ps.popleft()

        else:
            ps.append(ps.popleft())


##### review #####
def solution(priorities, location):
    answer = 0

    sp = sorted(priorities)
    pq = deque(enumerate(priorities))

    while sp:
        highest_priority = sp[-1]
        idx, priority = pq[0]

        if highest_priority == priority:
            answer += 1
            if location == idx:
                break
            pq.popleft()
            sp.pop()

        else:
            pq.append(pq.popleft())

    return answer
