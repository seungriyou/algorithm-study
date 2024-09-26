# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        binary search 응용
            (1) log n time에 minimum element 찾아야 하므로
            (2) 기본적으로 ascending order로 sorted 이므로

        mid & hi 비교 (원소는 모두 unique)
            nums[mid] > nums[hi]: (mid, hi]에 min element 존재
            nums[mid] < nums[hi]: [lo, mid]에 min element 존재
        """

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1  # (mid, hi]에 min element 존재
            else:
                hi = mid  # [lo, mid]에 min element 존재

        return nums[lo]
