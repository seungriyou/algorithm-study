# https://leetcode.com/problems/meeting-rooms/

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        intervals 오름차순 정렬
        -> e_i > s_i+1 이라면, 겹치는 것이므로 false return

        - TC: O(nlogn) (sort)
        - SC: O(n) (tim sort)
        """

        intervals.sort()

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True
