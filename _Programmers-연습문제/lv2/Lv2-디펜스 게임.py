# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq


def solution(n, k, enemy):
    """
    k 번의 무적권을 모두 사용해야 최대한 많은 라운드를 진행할 수 있음!
    q = 최소 힙으로 관리하며, 최종적으로 k 번의 무적권을 사용할 라운드의 enemy 값이 남게 됨 (길이가 k로 유지됨)
    """

    q = enemy[:k]
    heapq.heapify(q)

    for round in range(k, len(enemy)):
        n -= heapq.heappushpop(q, enemy[round])
        if n < 0:
            return round

    return len(enemy)


def solution2(n, k, enemy):
    # 무적권을 사용할 k번의 라운드 => 가장 큰 enemy 값 k개 모으기 (heapq)
    q = []
    cnt = 0

    for round, e in enumerate(enemy):
        # 최대힙에 현재 enemy 값 저장
        heapq.heappush(q, -e)

        # 사용해야 하는 병사 수 업데이트
        cnt += e

        # 현재 남은 병사가 부족한 경우
        if cnt > n:
            # 사용 가능한 무적권이 남지 않았다면 종료
            if not k:
                return round

            # 남은 k번 만큼 무적권 사용 가능
            k -= 1
            cnt += heapq.heappop(q)

    return len(enemy)
