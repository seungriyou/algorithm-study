# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        _sum, _max = sum(milestones), max(milestones)

        if _sum - _max < _max:
            return 2 * (_sum - _max) + 1
        else:
            return _sum

    def numberOfWeeks_TLE(self, milestones: List[int]) -> int:
        """TLE"""
        import heapq

        pq = [-ms for ms in milestones]
        heapq.heapify(pq)

        res = 0

        while len(pq) > 1:
            ms1 = heapq.heappop(pq)
            ms2 = heapq.heappop(pq)

            res += 2

            if (new_ms1 := ms1 + 1) != 0:
                heapq.heappush(pq, new_ms1)
            if (new_ms2 := ms2 + 1) != 0:
                heapq.heappush(pq, new_ms2)

        return res + 1 if pq else res
