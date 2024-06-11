# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_days = days[-1]
        dp = [0] * (max_days + 1)
        days = set(days)

        for day in range(1, max_days + 1):
            if day in days:
                dp[day] = min(
                    dp[max(day - 30, 0)] + costs[2],
                    dp[max(day - 7, 0)] + costs[1],
                    dp[max(day - 1, 0)] + costs[0]
                )
            else:
                dp[day] = dp[day - 1]

        return dp[max_days]
