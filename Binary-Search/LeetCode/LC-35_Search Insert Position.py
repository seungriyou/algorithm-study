# https://leetcode.com/problems/search-insert-position/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        target이 존재하면 index 반환, 존재하지 않으면 삽입될 위치 반환
        -> target 이상인 원소들 중 leftmost index
        """
        lo, hi = 0, len(nums)  # <- len(nums) 주의

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # if target > nums[mid]:
            #     lo = mid + 1
            # else:
            #     hi = mid    # look for left
            if target <= nums[mid]:
                hi = mid  # look for left
            else:
                lo = mid + 1

        return lo
