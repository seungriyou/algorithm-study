# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        """
        XOR 이용
        (1) [0, n] 값 모두 XOR
        (2) nums 값 모두 XOR
        -> 2번 등장한 값은 사라지고 1번 등장한 값만 남을 것

        - TC: O(n)
        - SC: O(1)
        """

        res = 0

        for i in range(1, len(nums) + 1):
            res ^= i
        for n in nums:
            res ^= n

        return res

    def missingNumber(self, nums: List[int]) -> int:
        """
        sum([0, n])을 구하고, sum(nums)를 빼면 된다
        -> sum([0, n]) == n * (n + 1) // 2

        - TC: O(n)
        - SC: O(1)
        """

        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
