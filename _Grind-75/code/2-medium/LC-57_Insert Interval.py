# https://leetcode.com/problems/insert-interval/
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        left, right = [], []

        for interval in intervals:
            s, e = interval

            # 현재 보고 있는 interval의 end가 newInterval의 start 보다 작다면, interval은 newInterval의 왼쪽에 위치
            if e < ns:
                left.append(interval)

            # 현재 보고 있는 interval의 start가 newInterval의 end 보다 작다면, interval은 newInterval의 오른쪽에 위치
            elif s > ne:
                right.append(interval)

            # 현재 보고 있는 interval과 newInterval이 겹친다면, newInterval과 interval 병합
            else:
                ns = min(ns, s)
                ne = max(ne, e)

        return left + [[ns, ne]] + right
    