# https://leetcode.com/problems/find-peak-element/

from typing import List


class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        """
        O(n)(linear search) 말고 O(logn)(binary search)로 풀어야 함
            - peak element: 인접한 element 보다 큰 값을 가지는 원소 (local maximum)
            - peak element가 여러 개여도 아무 값이나 하나 반환하면 됨
            - binary search를 적용할 수 있는 두 가지 상황
                (1) 원소가 정렬된 상황
                (2) 탐색 범위를 반씩 줄여나가며 O(logn)을 달성해야 하는 상황 (V)
            - binary search 로직
                - mid가 mid - 1, mid + 1보다 큰 값이라면 반환
                - 그렇지 않다면,
                    - mid - 1 > mid라면 왼쪽으로
                    - mid + 1 > mid라면 오른쪽으로
            - binary search를 통해 peak를 찾을 수 있다고 보장할 수 있는 이유
                (1) array의 바깥은 -inf이고
                (2) mid 보다 더 큰 값 쪽으로 이동하기 때문
                    -> 계속해서 값이 커지기만 하더라도, boundary에 도달하면 그 값이 peak가 됨!

        - lo < hi 보다 lo <= hi 로직을 사용하는 것이 peak를 발견했을 때 곧바로 반환하기에 더 직관적
        - mid - 1와 mid + 1를 mid와 비교하기 위해, boundary 부분을 우선 처리함
        """

        # base case(+ boundary 부분) 우선 확인
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1

        # boundary 부분 제외
        lo, hi = 1, n - 2

        while lo <= hi:
            mid = (lo + hi) // 2

            # mid가 peak 라면 mid 반환
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            # 그렇지 않다면, mid - 1와 mid + 1 중 mid 보다 큰 값 존재!
            # mid - 1이 mid 보다 크다면 왼쪽 살피기
            elif nums[mid - 1] > nums[mid]:
                hi = mid - 1
            # 그 외의 경우라면(mid + 1이 mid 보다 크다면) 오른쪽 살피기
            else:
                lo = mid + 1

    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2    # lower mid
            if nums[mid] > nums[mid + 1]:
                hi = mid  # include mid & look for left
            else:
                lo = mid + 1

        return lo

