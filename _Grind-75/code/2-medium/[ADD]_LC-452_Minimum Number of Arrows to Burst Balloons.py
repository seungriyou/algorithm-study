# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        intervals의 intersection을 모두 구하고, 그 개수를 반환하면 됨
        """

        # 최소 개수 반환
        if not points:
            return 0

        # 오름차순 정렬
        points.sort(key=lambda x: x[0])

        # 가장 최근(확인 중인) overlapped interval의 e
        end = float("inf")
        res = 1

        for s, e in points:
            # intersect X
            if end < s:
                res += 1
                end = e
            # intersect O
            else:
                end = min(end, e)

        return res

    def findMinArrowShots1(self, points: List[List[int]]) -> int:
        """
        e 기준으로 정렬하면, redundant 한 코드를 줄일 수 있다!!!
        ref: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/solutions/1686627/c-java-python-6-lines-sort-and-greedy-image-explanation
        """

        points.sort(key=lambda x: x[1])

        end = res = 0

        for s, e in points:
            # intersect X
            if res == 0 or end < s:
                res += 1
                end = e

        return res
    