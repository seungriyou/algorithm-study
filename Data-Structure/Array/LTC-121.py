# [LTC] 121 - Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # -- 문제의 constraint 대로
        min_price = sys.maxsize

        # -- prices를 순서대로 순회하면서 최소 가격 업데이트 & 최대 수익 업데이트
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))
