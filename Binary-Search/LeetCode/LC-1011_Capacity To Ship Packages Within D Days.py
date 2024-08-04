# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        least weight capacity
        - days 내에 모든 weights를 운반할 수 있어야 함
        - maximum weight capacity보다 더 많이 실을 수 없음

        feasible(capacity): 주어진 capacity 값에 대해, 모두 운반하는 데에 걸리는 일수가 days 이내인지 여부 반환하는 함수

        capacity의 least 값 구하기
            - lo: max(weights)
            - hi: sum(weights)
        """

        def feasible(capacity):
            """
            주어진 capacity에 대해 weights를 모두 운반하는 데에 걸리는 days 값 반환 ***
            """
            required_days, now_weight = 1, 0

            for w in weights:
                now_weight += w
                if now_weight > capacity:
                    required_days += 1
                    now_weight = w
                    if required_days > days:
                        return False

            return True

        lo, hi = max(weights), sum(weights)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if feasible(mid):
                hi = mid  # look for left
            else:
                lo = mid + 1  # exclude mid

        return lo

    def shipWithinDays1(self, weights: List[int], days: int) -> int:
        """
        least weight capacity
        - days 내에 모든 weights를 운반할 수 있어야 함
        - maximum weight capacity보다 더 많이 실을 수 없음

        get_required_days(capacity): 주어진 capacity 값에 대해, 모두 운반하는 데에 걸리는 days 값을 반환하는 함수

        capacity의 least 값 구하기
            - lo: max(weights)
            - hi: sum(weights)
        """

        def get_required_days(capacity):
            """
            주어진 capacity에 대해 weights를 모두 운반하는 데에 걸리는 days 값 반환 ***
            """
            required_days, now_weight = 1, 0

            for w in weights:
                now_weight += w
                if now_weight > capacity:
                    required_days += 1
                    now_weight = w

            return required_days

        lo, hi = max(weights), sum(weights)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if get_required_days(mid) > days:
                lo = mid + 1  # exclude mid
            else:
                hi = mid  # look for left

        return lo
