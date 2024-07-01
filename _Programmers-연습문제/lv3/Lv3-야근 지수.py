# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq


def solution(n, works):
    if n >= sum(works):
        return 0

    ws = [-work for work in works]
    heapq.heapify(ws)

    while ws and n > 0:
        _w = heapq.heappop(ws)

        n -= 1

        if _w + 1 < 0:
            heapq.heappush(ws, _w + 1)

    return sum(w * w for w in ws)
