# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

from typing import List


class Solution:
    def maxEvents1(self, events: List[List[int]]) -> int:
        import heapq

        # Sort events list by (1) start day and (2) end day in asc order
        events.sort()

        n = len(events)
        day = idx = cnt = 0

        # Create a min heap for end days of available events
        pq = []

        while idx < n or pq:
            # If pq is empty, set current start day
            if not pq:
                day = events[idx][0]

            # Add end days of all events starting today to pq
            while idx < n and events[idx][0] == day:
                heapq.heappush(pq, events[idx][1])
                idx += 1

            # If any event can be attended today, increase cnt
            heapq.heappop(pq)
            cnt += 1
            day += 1

            # Remove all events whose end day is earlier than today
            while pq and pq[0] < day:
                heapq.heappop(pq)

        return cnt

    def maxEvents(self, events: List[List[int]]) -> int:
        import heapq

        # Sort events list by (1) start day and (2) end day in asc order
        events.sort(reverse=True)

        day = cnt = 0

        # Create a min heap for end days of available events
        pq = []

        while events or pq:
            # If pq is empty, set current start day
            if not pq:
                day = events[-1][0]

            # Add end days of all events starting today to pq
            while events and events[-1][0] == day:
                heapq.heappush(pq, events.pop()[1])

            # If any event can be attended today, increase cnt
            heapq.heappop(pq)
            cnt += 1
            day += 1

            # Remove all events whose end day is earlier than today
            while pq and pq[0] < day:
                heapq.heappop(pq)

        return cnt
