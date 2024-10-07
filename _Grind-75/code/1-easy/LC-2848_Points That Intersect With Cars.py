# https://leetcode.com/problems/points-that-intersect-with-cars/

from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # 오름차순 정렬
        nums.sort()

        res = 0

        # non-overlapping intervals 찾기
        start = end = 0
        for s, e in nums:
            # initial
            if end == 0:
                start, end = s, e
            # non-overlap
            elif end < s:
                # 현재 interval에 해당하는 integer points의 개수 빼기
                res += (end - start + 1)
                # start & end 업데이트
                start, end = s, max(end, e)
            # overlap
            else:
                end = max(end, e)

        res += (end - start + 1)

        return res
