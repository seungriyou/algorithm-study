# [LTC] 80 - Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, cnt = 1, 1    # -- left = slow, right = fast, cnt = 해당 숫자가 등장하는 횟수

        for right in range(1, len(nums)):
            if nums[right - 1] == nums[right]:  # -- 동일한 숫자가 연달아 나오면 cnt 증가
                cnt += 1
            else:   # -- 그렇지 않으면 cnt = 1로 초기화
                cnt = 1

            # -- cnt > 2 이면 left는 움직이지 않고 right만 움직임
            if cnt <= 2:    # -- cnt <= 2이면 left 자리에 right 수 넣고 left 전진
                nums[left] = nums[right]
                left += 1

        return left

sol = Solution()
# nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
print(sol.removeDuplicates(nums))
print(nums)