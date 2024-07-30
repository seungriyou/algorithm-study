# https://leetcode.com/problems/counting-bits/

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        [ 0 ~ 1 ]
        bin(0) = 0
        bin(1) = 1

        [ 2 ~ 3 ]   -> offset = 2
        bin(2) = 10 = 10 + bin(0)
        bin(3) = 11 = 10 + bin(1)

        [ 4 ~ 7 ]   -> offset = 4
        bin(4) = 100 = 100 + bin(0)
        bin(5) = 101 = 100 + bin(1)
        bin(6) = 110 = 100 + bin(2)
        bin(7) = 111 = 100 + bin(3)

        [ 8 ~ 15 ]  -> offset = 8
        bin(8) = 1000 = 1000 + bin(0)
        ...
        bin(15) = 1111 = 1000 + bin(7)
        """

        dp = [0] * (n + 1)
        offset = 1

        for num in range(1, n + 1):
            if offset * 2 == num:
                offset *= 2

            dp[num] = dp[num - offset] + 1

        return dp
