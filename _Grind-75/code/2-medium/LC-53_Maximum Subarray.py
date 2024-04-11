# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_and_conquer(nums, i, j):
            """
            return value:
            - a = nums[i:j] 내에서 첫 번째 값을 포함하는 max contiguous sum
            - b = nums[i:j] 내에서 마지막 값을 포함하는 max contiguous sum
            - m = nums[i:j] 내에서 max contiguous sum
            - s = nums[i:j]의 전체 합
            """
            # base condition
            if i == j - 1:
                return nums[i], nums[i], nums[i], nums[i]

            # (1) divide
            # get middle
            mid = (i + j) // 2

            # left half
            la, lb, lm, ls = divide_and_conquer(nums, i, mid)

            # right half
            ra, rb, rm, rs = divide_and_conquer(nums, mid, j)

            # (2) conquer
            a = max(la, ls + ra)
            b = max(rb, rs + lb)
            m = max(lm, rm, lb + ra)
            s = ls + rs

            return a, b, m, s

        _, _, max_sum, _ = divide_and_conquer(nums, 0, len(nums))

        return max_sum

    def maxSubArray_kadane(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)

    def maxSubArray_dp_o1(self, nums: List[int]) -> int:
        prev = max_sum = nums[0]

        for i in range(1, len(nums)):
            prev = max(nums[i], nums[i] + prev)
            max_sum = max(max_sum, prev)

        return max_sum

    def maxSubArray_dp_on(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dp[i - 1], 0)
            max_sum = max(max_sum, dp[i])

        return max_sum

###### review ######
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """O(1)"""

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)

    def maxSubArray2(self, nums: List[int]) -> int:
        """O(1)"""

        max_sum = prev = nums[0]

        for i in range(1, len(nums)):
            prev = max(prev + nums[i], nums[i])
            max_sum = max(max_sum, prev)

        return max_sum

    def maxSubArray1(self, nums: List[int]) -> int:
        """O(N)"""

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i - 1]) + nums[i]

        return max(dp)
