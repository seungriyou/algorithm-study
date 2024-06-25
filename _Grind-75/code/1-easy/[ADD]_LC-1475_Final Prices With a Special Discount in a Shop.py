# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """monotonic stack"""

        res = prices[:]

        # increasing monotonic stack
        stack = []

        for i, price in enumerate(prices):
            # prices[j] <= prices[i]인 것 중 min index를 골라야하므로
            while stack and prices[stack[-1]] >= price:
                res[stack.pop()] -= price
            stack.append(i)

        return res

    def finalPrices2(self, prices: List[int]) -> List[int]:
        """brute-force"""

        res = prices[:]

        for i, price in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= price:
                    res[i] -= prices[j]
                    break

        return res
