# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        기본적으로 오름차순 정렬이므로, mid와 hi를 비교하면 된다.

        - mid > hi 인 경우
            3 4 5 6 0 1 2   -> min 값은 (mid, hi] 범위에 존재
            l     m ^   h   => l = m + 1

        - mid < hi 인 경우
            5 6 0 1 2 3 4   -> min 값은 [lo, mid] 범위에 존재
            l   ^ m     h   => h = m

            4 5 6 0 1 2 3
            l     m     h

            0 1 2 3 4 5 6
            l     m     h
        """

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] < nums[hi]:
                # min 값은 [lo, mid]에 존재할 수 있음
                hi = mid
            else:
                # min 값은 (mid, hi]에 존재할 수 있음
                lo = mid + 1

        return nums[lo]
