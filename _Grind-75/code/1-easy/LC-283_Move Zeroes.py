# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        two pointer
            lo = 가장 왼쪽에 위치한 zero
            hi = non-zero 값
        """

        lo = 0
        for hi in range(len(nums)):
            # nums[hi]가 0이면 넘어가기 (hi는 non-zero)
            if nums[hi] == 0:
                continue
            # nums[lo]가 0이 될 때까지 이동하기 (lo는 zero)
            while lo < hi and nums[lo] != 0:
                lo += 1
            # lo와 hi swap 하기
            nums[lo], nums[hi] = nums[hi], nums[lo]

    def moveZeroes(self, nums: List[int]) -> None:
        """더 수정한 버전"""

        lo = 0
        for hi in range(len(nums)):
            # hi가 non-zero를 가리킨다면 lo와 swap
            if nums[hi] != 0:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                # 기존의 lo 자리는 이미 채워졌으므로 ++
                lo += 1
