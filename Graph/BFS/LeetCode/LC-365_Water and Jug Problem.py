# [LTC] 365 - Water and Jug Problem
# https://leetcode.com/problems/water-and-jug-problem/

from collections import deque


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        q = deque([(0, 0)])  # -- state of two jugs (now, empty jugs)
        visited = set((0, 0))

        while q:
            jug1, jug2 = q.popleft()
            if jug1 + jug2 == targetCapacity:
                return True

            states = set()
            states.add((jug1Capacity, jug2))  # -- (1) jug1 채우기
            states.add((jug1, jug2Capacity))  # -- (2) jug2 채우기
            states.add((0, jug2))  # -- (3) jug1 버리기
            states.add((jug1, 0))  # -- (4) jug2 버리기
            states.add((  # -- (5) jug2를 jug1에 붓기
                min(jug1 + jug2, jug1Capacity),
                0 if jug2 < jug1Capacity - jug1 else jug2 - (jug1Capacity - jug1)))
            states.add((  # -- (6) jug1을 jug2에 붓기
                0 if jug1 < jug2Capacity - jug2 else jug1 - (jug2Capacity - jug2),
                min(jug1 + jug2, jug2Capacity)))

            for state in states:
                if state in visited:
                    continue
                q.append(state)
                visited.add(state)

        return False

    def canMeasureWater2(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
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
