# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo + 1) // 2

            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid

        return lo if nums[lo] == target else -1

    def search2(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        return hi if nums[hi] == target else -1
