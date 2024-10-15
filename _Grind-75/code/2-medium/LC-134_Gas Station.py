# https://leetcode.com/problems/gas-station/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # impossible (only case) -- (gas[i] - cost[i])의 총합이 음수라면 불가능
        if sum(gas) < sum(cost):
            return -1

        tank = start_idx = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            # 만약 i-th station에서 tank가 음수, 즉 불가능한 경우가 생긴다면 start idx 업데이트 & tank 초기화
            if tank < 0:
                start_idx = i + 1  # 현재 idx인 i는 start idx가 될 수 없으므로 다음 값으로 지정
                tank = 0

        return start_idx
    