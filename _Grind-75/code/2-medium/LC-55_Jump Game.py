# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump1(self, nums: List[int]) -> bool:
        """
        DP - too slow (TC O(n^2)인데 돌아는 간다?!)
        dp[i] = i idx로부터 last idx까지 도달 가능한지 여부

        TC: O(n^2)
        SC: O(n)
        """

        n = len(nums)

        # dp[i] = i idx로부터 last idx까지 도달 가능한지 여부
        dp = [False] * (n)
        dp[-1] = True

        for i in range(n - 2, -1, -1):
            for j in range(nums[i] + 1):
                if dp[i + j]:
                    dp[i] = True
                    break

        return dp[0]

    def canJump2(self, nums: List[int]) -> bool:
        """
        greedy
        ref: https://leetcode.com/problems/jump-game/solutions/4534808/super-simple-intuitive-8-line-python-solution-beats-99-92-of-users

        TC: O(n)
        SC: O(1)
        """
        steps = 0

        for n in nums:
            if steps < 0:
                return False
            elif n > steps:
                steps = n

            steps -= 1

        return True

    def canJump(self, nums: List[int]) -> bool:
        """
        DP + Greedy - faster
        ref: https://leetcode.com/problems/jump-game/solutions/596454/python-simple-solution-with-thinking-process-runtime-o-n

        TC: O(n)
        SC: O(1)
        """
        n = len(nums)

        # last idx에 도달 가능한 가장 큰 idx
        last_idx = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last_idx:
                last_idx = i

        return last_idx == 0
