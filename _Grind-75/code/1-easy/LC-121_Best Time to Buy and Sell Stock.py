# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, int(1e4)

        for price in prices:
            # 최소 가격 tracking
            min_price = min(min_price, price)
            # 최대 수익 업데이트
            max_profit = max(max_profit, price - min_price)

        return max_profit
