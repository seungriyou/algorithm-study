# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement_sort(self, nums: List[int]) -> int:
        """
        sort 후 정 가운데에 위치한 원소 == 과반수 이상 등장하는 원소
        """
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement_bm1(self, nums: List[int]) -> int:
        """
        boyer-moore majority vote algorithm (O(n) time & O(1) space)
        """
        major = nums[0]

        cnt = 1
        for i in range(1, len(nums)):
            if major == nums[i]:
                cnt += 1
            elif cnt == 0:
                major, cnt = nums[i], 1
            else:
                cnt -= 1

        return major

    def majorityElement(self, nums: List[int]) -> int:
        """
        boyer-moore majority vote algorithm (O(n) time & O(1) space)
        """
        cnt = major = 0

        for num in nums:
            if cnt == 0:
                major = num

            if major == num:
                cnt += 1
            else:
                cnt -= 1

        return major
