# [LTC] 162 - Find Peak Element
# https://leetcode.com/problems/find-peak-element/

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        l, h = 1, n - 2

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            # mid 보다 더 큰 값이 있는 쪽을 확인해야 함
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                h = mid - 1

nums = [1,2,1,3,5,6,4]
sol = Solution()
print(sol.findPeakElement(nums))
