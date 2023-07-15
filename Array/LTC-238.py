# [LTC] 238 - Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        # -- 각 인덱스의 왼쪽만 곱한 값 채우기
        prod = 1
        for i in range(len(nums)):
            out.append(prod)
            prod *= nums[i]
        # -- 각 인덱스의 오른쪽만 곲한 값 곱하기
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= prod
            prod *= nums[i]

        return out

nums = [-1,1,0,-3,3]
sol = Solution()
print(sol.productExceptSelf(nums))
