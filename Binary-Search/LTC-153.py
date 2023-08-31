# [LTC] 153 - Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [1] 3 4 5 (1 2)
            l   m    h   : mid > hi 인 경우, l = m + 1

        [2] (1 2 3) 4 5
             l   m   h

            (5 1 2) 3 4
             l   m   h

            (4 5 1) 2 3
             l   m   h   : mid < hi 인 경우, mid가 min value일 수 있므로 h = m
        """
        l, h = 0, len(nums) - 1

        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m

        return nums[l]

sol = Solution()
nums = [4,5,6,7,0,1,2]
print(sol.findMin(nums))
