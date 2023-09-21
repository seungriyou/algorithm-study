# [LC] 213 - House Robber II
# https://leetcode.com/problems/house-robber-ii/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # === not using dp array ===
        n = len(nums)
        if n <= 3:
            return max(nums)

        f_prev1 = f_prev2 = 0  # -- 첫 원소 없이 (nums[1:])
        l_prev1 = l_prev2 = 0  # -- 마지막 원소 없이 (nums[:-1])

        for i in range(n - 1):
            # 첫 원소가 없는 경우, i = 1 ~ n-1 여야하므로 +1 해주기
            # 마지막 원소가 없는 경우, i = 0 ~ n-2
            f_prev2, f_prev1 = f_prev1, max(f_prev2 + nums[i + 1], f_prev1)
            l_prev2, l_prev1 = l_prev1, max(l_prev2 + nums[i], l_prev1)

        return max(f_prev1, l_prev1)

    def rob_twice(self, nums: List[int]) -> int:
        '''
        첫 원소 없이 dp 이용해서 구한 maximum amount와
        마지막 원소 없이 dp 이용해서 구한 maximum amount 중
        큰 값이 정답이다.
        (첫 원소와 마지막 원소 둘 다 count 하면 안되므로)
        '''
        n = len(nums)
        if n <= 3:
            return max(nums)

        dp1 = [-1] * (n - 1)  # -- 첫 원소 없이
        dp2 = [-1] * (n - 1)  # -- 마지막 원소 없이

        dp1[0] = nums[1]
        dp2[0] = nums[0]
        if n - 1 > 1:
            dp1[1] = max(dp1[0], nums[2])
            dp2[1] = max(dp2[0], nums[1])

        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i + 1])
        for i in range(2, n - 1):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

        return max(dp1[-1], dp2[-1])

nums = [1,2,3,1]
sol = Solution()
print(sol.rob(nums))
