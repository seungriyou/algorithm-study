# https://leetcode.com/problems/koko-eating-bananas/

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        koko가 h시간 내에 바나나를 모두 먹을 수 있는 minimum integer k 구하기
            - k = bananas-per-hour eating speed
            - guards는 h시간에 한 번 방문
            - 해당 pile에 바나나가 k개 미만이면 그만큼만 먹을 수 있음
            - 각 시간에 하나의 pile만 먹을 수 있음

        feasible(speed): 주어진 speed로 바나나를 h 시간 내에 모두 다 먹을 수 있는지 여부 반환

        minimum integer bananas-per-hour eating speed
            - lo: 1
            - hi: max(piles)
        """

        def feasible(speed):
            """
            required_hours = 0

            for pile in piles:
                q, r = divmod(pile, speed)
                required_hours += q + (1 if r else 0)
                if required_hours > h:
                    return False

            return True
            """
            # faster (ceil) ****
            return sum((pile - 1) // speed + 1 for pile in piles) <= h

        lo, hi = 1, max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid  # look for left
            else:
                lo = mid + 1

        return lo

    def minEatingSpeed1(self, piles: List[int], h: int) -> int:
        """
        koko가 h시간 내에 바나나를 모두 먹을 수 있는 minimum integer k 구하기
            - k = bananas-per-hour eating speed
            - guards는 h시간에 한 번 방문
            - 해당 pile에 바나나가 k개 미만이면 그만큼만 먹을 수 있음
            - 각 시간에 하나의 pile만 먹을 수 있음

        get_required_hours_to_eat_bananas(speed): 주어진 speed로 바나나를 모두 다 먹을 수 있는 시간 반환

        minimum integer bananas-per-hour eating speed
            - lo: 1
            - hi: max(piles)
        """

        def get_required_hours_to_eat_bananas(speed):
            required_hours = 0

            for pile in piles:
                q, r = divmod(pile, speed)
                required_hours += q + (1 if r else 0)

            return required_hours

        lo, hi = 1, max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if get_required_hours_to_eat_bananas(mid) > h:
                lo = mid + 1
            else:
                hi = mid  # look for left

        return lo
