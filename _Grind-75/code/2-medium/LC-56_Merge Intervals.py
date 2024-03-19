# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = []

        for intv in intervals:
            if merged_intervals and merged_intervals[-1][1] >= intv[0]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], intv[1])
            else:
                merged_intervals.append(intv)

        return merged_intervals
