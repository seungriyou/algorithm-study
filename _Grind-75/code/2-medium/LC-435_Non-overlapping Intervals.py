# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [sol1] sort & greedy (O(nlogn) for sorting)
               (monotonic stack?)

        각 interval의 시작과 끝 시각을 [s, e]라고 하자.
        이때, 항상 빠른 e를 골라야지만 가장 적은 수의 interval을 제거하여 non-overlapping intervals를 남길 수 있다.
        이는 빠른 e를 가진 interval을 남겨야 다른 intervals를 더 많이 수용할 수 있기 때문이다.

        따라서 주어진 intervals를 e 기준으로 오름차순 정렬한 후 순회하면서
        현재 보고 있는 interval을 [s, e]라고 하고, 지금까지 남긴 intervals의 e 중 가장 큰 값(= 가장 최근에 남긴 interval의 e)을 end라고 두자.
        - s < end:  overlap
          -> (1) 현재 보고 있는 interval이 가장 최근에 남긴 interval과 겹치고 (2) end <= e이므로 (오름차순 정렬)
             현재 보고 있는 interval은 제거 (cnt++)
        - s >= end: non-overlap
          -> 가장 최근에 남긴 interval과 겹치지 않으므로 제거하지 않고, end를 e로 업데이트
        """

        end, res = float('-inf'), 0

        for s, e in sorted(intervals, key=lambda x: x[1]):
            # overlap - 현재 보고 있는 interval 제거
            if s < end:
                res += 1
            # non-overlap - end 값 업데이트
            else:
                end = e

        return res

    def eraseOverlapInterval2(self, intervals: List[List[int]]) -> int:
        """
        [sol2] DP & binary search
        ref: https://leetcode.com/problems/non-overlapping-intervals/solutions/3788241/c-java-easy-and-clean-code-dp-greedy-beats
             https://leetcode.com/problems/non-overlapping-intervals/solutions/1489142/python-dp-find-the-maximum-non-overlapping-intervals-o-n-diff-greedy-with-picture

        - intervals를 start 기준으로 오름차순 정렬하여, 마지막 interval 부터 확인해나감
          current interval을 지울지 유지할지를 결정할 때, future interval을 고려해야 하기 때문에 필요!
        """

        n = len(intervals)

        def find_lower_bound(idx):
            """
            intervals에서
                (1) target(= current interval의 end) 이후에 start를 가지고 있으면서
                (2) 가장 빠른
            interval의 index를 찾는 함수
            """
            curr_end = intervals[idx][1]
            lo, hi = idx + 1, n

            while lo < hi:
                mid = lo + (hi - lo) // 2
                if intervals[mid][0] < curr_end:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        # intervals를 start 기준으로 오름차순 정렬
        intervals.sort(key=lambda x: x[0])

        # dp[i] = sorted intervals에서 index i 이후에 위치한 intervals가 non-overlapping이 되도록
        #         제거해야 하는 intervals의 minimum 개수
        #         i == n일 때는 out of bound이므로, dp[n] = 0가 되도록 하기 위해 * (n + 1)
        dp = [0] * (n + 1)

        # intervals를 뒤에서부터 확인
        for idx in range(n - 1, -1, -1):
            # current interval 다음에 위치하는 "첫 non-overlapping interval"을 찾음
            # 즉, current interval을 keep 한 다음에 선택할 next interval의 index를 얻음
            next_idx = find_lower_bound(idx)

            # (1) keep current interval
            #   - dp[next_idx] = next non-overlapping interval의 dp 값
            #   - (next_idx - idx - 1) = current interval과 next non-overlapping interval 사이에 위치한
            #                            overlapping intervals의 개수 (current interval을 택한다면 overlap 될 intervals 제외하기)
            v1 = dp[next_idx] + (next_idx - idx - 1)
            # (2) remove current interval
            v2 = dp[idx + 1] + 1

            # update dp table
            dp[idx] = min(v1, v2)

        return dp[0]
