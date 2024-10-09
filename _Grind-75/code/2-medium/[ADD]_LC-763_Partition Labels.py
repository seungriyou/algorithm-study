# https://leetcode.com/problems/partition-labels/

from typing import List


class Solution:
    def partitionLabels1(self, s: str) -> List[int]:
        """
        - 문자마다 맨 처음 & 마지막으로 등장하는 인덱스 찾기 -> interval로 기록
        - overlapped intervals 합치기 (#56 참고)
        """

        from collections import defaultdict

        # 문자마다 맨 처음 & 마지막으로 등장하는 인덱스를 찾아 intervals로 만들기
        starts, ends = defaultdict(int), defaultdict(int)
        for i, _s in enumerate(s):
            if _s not in starts:
                starts[_s] = i
            ends[_s] = i

        intervals = []
        for _s in starts:
            intervals.append([starts[_s], ends[_s]])

        # intervals 오름차순 정렬
        intervals.sort()

        # overlapped intervals 합치기
        res = []
        for s, e in intervals:
            # non-overlap
            if not res or res[-1][1] < s:
                res.append([s, e])
            # overlap
            else:
                res[-1][1] = max(res[-1][1], e)

        return [e - s + 1 for s, e in res]

    def partitionLabels(self, s: str) -> List[int]:
        """
        two-pointer 풀이 (w/o sorting)
        ref: https://leetcode.com/problems/partition-labels/solutions/298474/python-two-pointer-solution-with-explanation
        """

        # 각 문자의 가장 마지막 등장 index 기록
        ends = {c: i for i, c in enumerate(s)}

        # two pointers (for tracking last non-overlapping interval)
        lo = hi = 0

        res = []

        for i, c in enumerate(s):
            # 새롭게 찾을 non-overlapping interval의 hi 업데이트
            hi = max(hi, ends[c])

            # 만약 현재 문자가 non-overlapping interval의 마지막 문자라면 기록
            if i == hi:
                res.append(hi - lo + 1)
                lo = hi + 1

        return res
