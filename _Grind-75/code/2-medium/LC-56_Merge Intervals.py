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


###### review ######
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        for s, e in intervals:
            # res가 비어있거나, 가장 최근 interval의 e가 s보다 작을 때, 겹치지 X
            if not res or res[-1][1] < s:
                res.append([s, e])
            # 그렇지 않다면 기존의 가장 최근 interval의 e를 '더 큰 값'으로 업데이트 (주의!)
            else:
                res[-1][1] = max(res[-1][1], e)

        return res


###### review 2 ######
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # non-overlapping intervals를 모을 list
        res = []

        # intervals를 오름차순 정렬
        intervals.sort()

        # intervals를 순회하며, overlap인 경우는 합치고 non-overlap인 경우는 새롭게 기록
        for s, e in intervals:
            # non-overlap 인 경우
            if not res or res[-1][1] < s:
                res.append([s, e])
            # overlap 인 경우
            else:
                res[-1][1] = max(res[-1][1], e)

        return res
