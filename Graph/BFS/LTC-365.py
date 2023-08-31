# [LTC] 365 - Water and Jug Problem
# https://leetcode.com/problems/water-and-jug-problem/

from collections import deque

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        """
        두 jar 사이에 water를 주고 받는 것은 전혀 상관 X
        물을 각 jar만큼 채우느냐/버리느냐만 중요함

        ex) jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
            (1) +3
            (2) +3
            (3) -5
            (4) +3
        """

        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        q = deque([0])
        visited = {0}
        capacity_changes = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]

        while q:
            curr_capacity = q.popleft()

            for capacity_change in capacity_changes:
                tmp_capacity = curr_capacity + capacity_change

                if tmp_capacity == targetCapacity:
                    return True

                if tmp_capacity not in visited and 0 <= tmp_capacity <= jug1Capacity + jug2Capacity:
                    q.append(tmp_capacity)
                    visited.add(tmp_capacity)

        return False

sol = Solution()
jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4
print(sol.canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))
