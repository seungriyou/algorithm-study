# https://leetcode.com/problems/meeting-rooms-ii/

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [sort & pointer]

        - TC: O(nlogn)
        - SC: O(n)
        """
        e = res = 0  # e = points first available room
        start = sorted(s for s, _ in intervals)
        end = sorted(e for _, e in intervals)

        for s in range(len(intervals)):
            # overlap -> res++
            if start[s] < end[e]:
                res += 1
            # next available room
            else:
                e += 1

        return res

    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        """
        [greedy & priority queue]

        - TC: O(nlogn)
        - SC: O(n)
        """
        import heapq

        # end time
        rooms = []

        # sort
        intervals.sort()

        for s, e in intervals:
            if rooms and rooms[0] <= s:
                heapq.heappop(rooms)
            heapq.heappush(rooms, e)

        return len(rooms)
