# https://leetcode.com/problems/next-permutation/

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        - TC: O(n)
        - SC: O(1)
        """

        # start 이후의 index에 대해 reverse 하는 함수
        def reverse(nums, start):
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # 오른쪽에서부터 처음으로 decrease 하는 원소의 index인 i 찾기
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 처음으로 decrease 하는 원소가 있다면
        if i >= 0:
            # (1) i 보다 오른쪽에 있으면서 (2) nums[i] 보다 큰 원소들 중에 (3) 가장 작은 원소의 index인 j 찾기
            # 오른쪽에서부터 increasing 이므로, 오른쪽에서부터 nums[i] < nums[j] 순간까지 한칸씩 왼쪽으로 이동하면 됨
            j = len(nums) - 1
            while nums[i] >= nums[j]:
                j -= 1

            # i와 j swap 하기
            nums[i], nums[j] = nums[j], nums[i]

        # i의 오른쪽을 reverse 하기
        reverse(nums, i + 1)
