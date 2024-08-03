# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        # find leftmost
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid  # look for left

        # early stopping
        if lo == len(nums) or nums[lo] != target:
            return ans

        ans[0] = lo

        # find rightmost (w/ lo already found)
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid  # look for right

        ans[1] = hi

        return ans
