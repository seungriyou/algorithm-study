# [PG] 42626 - 더 맵게 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (2 * second))
        cnt += 1

    return cnt


def solution2(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    if scoville[0] >= K:
        return cnt

    while len(scoville) >= 2:
        first, second = heapq.heappop(scoville), heapq.heappop(scoville)
        new_scoville = first + (2 * second)
        heapq.heappush(scoville, new_scoville)
        cnt += 1

        if scoville[0] >= K:  # -- 최솟값만 K 이상인지 확인하면 ok
            return cnt

    return -1


def solution3(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    if scoville[0] >= K:
        return 0

    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + 2 * second

        heapq.heappush(scoville, new_scoville)
        cnt += 1

        if scoville[0] >= K:
            return cnt

    return -1


scoville = [1, 2, 3, 9, 10, 12]
K = 7
assert 2 == solution(scoville[:], K) == solution2(scoville[:], K)
