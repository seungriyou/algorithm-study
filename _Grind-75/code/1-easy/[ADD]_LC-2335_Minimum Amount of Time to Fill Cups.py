# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        import heapq

        pq = [-amnt for amnt in amount if amnt != 0]
        heapq.heapify(pq)

        time = 0

        while len(pq) > 1:
            amnt1 = heapq.heappop(pq)
            amnt2 = heapq.heappop(pq)

            if amnt1 != -1:
                heapq.heappush(pq, amnt1 + 1)
            if amnt2 != -1:
                heapq.heappush(pq, amnt2 + 1)

            time += 1

        if pq:
            time -= heapq.heappop(pq)

        return time
