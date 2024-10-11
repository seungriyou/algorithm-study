# https://leetcode.com/problems/teemo-attacking/

from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        overlapping intervals를 merge 하고, 결과로 얻은 non-overlapping intervals의 전체 길이를 세면 됨
        """

        if not timeSeries or not duration:
            return 0

        # 결과값으로 가능한 최소 값
        res = duration

        # 인접한 두 time 값의 차와 duration 값 중 작은 값을 res에 더하기
        for t1, t2 in zip(timeSeries, timeSeries[1:]):
            res += min(t2 - t1, duration)  # min(overlap(= refresh), non-overlap)

        return res
