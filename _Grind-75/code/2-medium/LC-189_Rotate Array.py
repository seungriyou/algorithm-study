# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        O(1) extra space

            A1 ... An-k | An-k+1 ... An
        ->  An ... An-k+1 | An-k ... A1 (전체 뒤집기)
        ->  An-k+1 ... An | A1 ... An-k (k를 기준으로 나눠진 구간 각각 뒤집기)
        """

        n = len(nums)
        k %= n

        def reverse(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        if k:
            # 1. 전체 뒤집기
            reverse(0, n - 1)
            # 2. k를 기준으로 나누어진 두 구간 각각 뒤집기
            reverse(0, k - 1)
            reverse(k, n - 1)

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        O(n) extra space
        """
        k %= len(nums)

        if k:
            moved = nums[-k:]

            for i in range(len(nums) - k - 1, -1, -1):
                nums[i + k] = nums[i]

            for i in range(k):
                nums[i] = moved[i]
