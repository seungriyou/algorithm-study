# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        # (1) -> 방향 순회: 현재 원소의 왼쪽에 있는 원소들의 곱 구하면서 result 업데이트
        prod = 1
        for i in range(len(nums)):
            result.append(prod)
            prod *= nums[i]

        # (2) <- 방향 순회: 현재 원소의 오른쪽에 있는 원소들의 곱 구하면서 result 업데이트
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= prod
            prod *= nums[i]

        return result

    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # (1) -> 방향 순회: 현재 원소의 왼쪽에 있는 원소들의 곱 구하면서 result 업데이트
        p = 1
        for i in range(n - 1):
            p *= nums[i]
            result[i + 1] *= p

        # (2) <- 방향 순회: 현재 원소의 오른쪽에 있는 원소들의 곱 구하면서 result 업데이트
        p = 1
        for i in range(n - 1, 0, -1):
            p *= nums[i]
            result[i - 1] *= p

        return result
