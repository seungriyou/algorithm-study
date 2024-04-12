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


###### review ######
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals는 이미 start 기준으로 정렬되어 있음!

        left, right = [], []
        # left: end < newInterval[0]
        # right: start > newInterval[1]

        ns, ne = newInterval

        for s, e in intervals:
            # left에 해당한다면,
            if e < ns:
                left.append([s, e])

            # right에 해당한다면,
            elif s > ne:
                right.append([s, e])

            # newInterval과 겹친다면, ns & ne 업데이트
            else:
                ns = min(ns, s)
                ne = max(ne, e)

        return left + [[ns, ne]] + right
