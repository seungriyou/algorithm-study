# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        원소가 distinct 했던 이전 문제는 다음과 같이 풀었다.
            크게 두 가지 케이스를 나누어서 생각할 수 있다.
                (1) 왼쪽 구간이 monotonic 한 경우 (nums[lo] <= nums[mid], lower mid를 사용하므로 <= 여야 함에 주의!)
                    - 왼쪽 구간(lo ~ mid)에 target이 속한다면 왼쪽 구간을,
                    - 아니라면 오른쪽 구간을 살피기
                (2) 오른쪽 구간이 monotonic 한 경우
                    - 오른쪽 구간(mid ~ hi)에 target이 속한다면 오른쪽 구간을,
                    - 아니라면 왼쪽 구간을 살피기

        이번 문제는 duplicate을 허용하기 때문에, 이로 인해 어느 구간을 탐색해야 할지 결정할 수 없는 경우를 추가로 처리해야 한다.
            - nums[lo] == nums[mid] 인 경우: 다음과 같은 두 경우가 가능하다.
                (1) 1, 1, 1, 1, 2, 3, 4     -> lo++로 넘어가기
                    l        m        h
                (2) 1, 2, 3, 1, 1, 1, 1     -> lo++ && hi--로 넘어가기
                    l        m        h
            - nums[mid] == nums[hi] 인 경우: 다음과 같은 두 경우가 가능하다.
                (1) 2, 2, 3, 1, 1, 1, 1     -> hi--로 넘어가기
                    l        m        h
                (2) 1, 2, 3, 1, 1, 1, 1     -> lo++ && hi--로 넘어가기
                    l        m        h
        """

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # target 발견 시 곧바로 반환
            if nums[mid] == target:
                return True

            # lo ~ mid 까지 monotonic 한 경우 (<=에서 <로 변경 주의!)
            elif nums[lo] < nums[mid]:
                # lo ~ mid 에 target이 속하는 경우, 왼쪽 살피기
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # mid ~ right 까지 monotonic 한 경우
            elif nums[mid] < nums[hi]:
                # mid ~ hi 에 target이 속하는 경우, 오른쪽 살피기
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            # [추가된 로직] duplicate 처리
            else:
                if nums[lo] == nums[mid]:
                    lo += 1
                if nums[mid] == nums[hi]:
                    hi -= 1

        return False
