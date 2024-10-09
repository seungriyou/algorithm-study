# https://leetcode.com/problems/interval-list-intersections/

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        [ two-pointer ]
        ref: https://leetcode.com/problems/interval-list-intersections/solutions/647482/python-two-pointer-approach-thinking-process-diagrams
        두 interval [s1, e1], [s2, e2]가 서로 겹치는 경우는
        (s1 > e2 || e1 < s2) 인 경우에 해당하지 않을 때이다!
        => 즉, (s1 <= e2 && e1 >= s2) 인 경우라면 겹친다.

        또한, 겹치는 interval의 구간은
        [max(s1, s2), min(e1, e2)] 가 된다.
        """

        i = j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]

            # 두 interval이 겹치는 경우
            if s1 <= e2 and e1 >= s2:
                # 겹치는 구간 기록
                res.append([max(s1, s2), min(e1, e2)])

            # [s1, e1]과 [s2, e2] 중 e가 큰쪽을 다음 단계에도 더 살펴보아야 함
            if e1 <= e2:
                i += 1
            else:
                j += 1

        return res
