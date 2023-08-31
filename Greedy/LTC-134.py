# [LTC] 134 - Gas Station
# https://leetcode.com/problems/gas-station/

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # sum(gas) >= sum(cost) 이면 solution이 존재함
        if sum(gas) < sum(cost):
            return -1

        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1

        return start

sol = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas, cost))
