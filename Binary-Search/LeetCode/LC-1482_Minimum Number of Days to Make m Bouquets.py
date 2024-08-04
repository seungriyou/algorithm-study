# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # early stop
        if m * k > len(bloomDay):
            return -1

        def feasible(day):
            """
            feasible(day): day 내에 m개 이상의 부케를 만들 수 있는지 여부
                - 현재 day에 피어있는 꽃들 확인
                - 인접한 꽃들을 대상으로, k개가 인접한 경우를 모두 모아 만들 수 있는 부케의 개수 세기
                - 부케의 개수
            """
            bouquets, flowers = 0, 0

            for d in bloomDay:
                # 현재 피지 않았으면 flowers 초기화 후 넘어가기
                if d > day:
                    flowers = 0
                    continue

                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
                # q, r = divmod(flowers + 1, k)
                # bouquets += q
                # flowers = r

            return bouquets >= m

        lo, hi = min(bloomDay), max(bloomDay)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if feasible(mid):
                hi = mid  # look for left
            else:
                lo = mid + 1

        return lo

    def minDays1(self, bloomDay: List[int], m: int, k: int) -> int:
        # early stop
        if m * k > len(bloomDay):
            return -1

        def get_number_of_bouquets(day):
            """
            get_number_of_bouquets(day): day 내에 만들 수 있는 부케 개수 반환
                - 현재 day에 피어있는 꽃들 확인
                - 인접한 꽃들을 대상으로, k개가 인접한 경우를 모두 모아 만들 수 있는 부케의 개수 세기
            """
            bouquets, flowers = 0, 0

            for d in bloomDay:
                # 현재 피지 않았으면 curr_flower 초기화 후 넘어가기
                if d > day:
                    flowers = 0
                    continue

                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
                # q, r = divmod(flowers + 1, k)
                # bouquets += q
                # flowers = r

            return bouquets

        lo, hi = min(bloomDay), max(bloomDay)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if get_number_of_bouquets(mid) < m:
                lo = mid + 1
            else:
                hi = mid  # look for left

        return lo
