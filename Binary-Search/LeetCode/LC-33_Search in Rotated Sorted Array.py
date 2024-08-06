# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        크게 두 가지 케이스를 나누어서 생각할 수 있다.
            (1) 왼쪽 구간이 monotonic 한 경우 (nums[lo] <= nums[mid], lower mid를 사용하므로 <= 여야 함에 주의!)
                - 왼쪽 구간(lo ~ mid)에 target이 속한다면 왼쪽 구간을,
                - 아니라면 오른쪽 구간을 살피기
            (2) 오른쪽 구간이 monotonic 한 경우
                - 오른쪽 구간(mid ~ hi)에 target이 속한다면 오른쪽 구간을,
                - 아니라면 왼쪽 구간을 살피기
        """
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # target 발견 시 곧바로 반환
            if nums[mid] == target:
                return mid

            # lo ~ mid 까지 monotonic 한 경우 (<= 임에 주의!)
            if nums[lo] <= nums[mid]:
                # lo ~ mid 에 target이 속하는 경우, 왼쪽 살피기
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # mid ~ right 까지 monotonic 한 경우
            else:
                # mid ~ hi 에 target이 속하는 경우, 오른쪽 살피기
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1

    def search1(self, nums: List[int], target: int) -> int:
        """
        lo <= hi 루프를 돌면서, target에 해당하는 값을 찾은 경우 곧바로 반환하도록 한다.

        크게 두 가지 케이스를 나누어서 생각할 수 있다.
            (1) 원래라면 왼쪽 구간을 살펴봐야 하는 경우: target < nums[mid]
                - 왼쪽 구간(lo ~ mid)이 monotonic 하지만, 그 구간에 속하지 않는다면 오른쪽 구간을 살펴봐야 함
                - 그 외의 경우에는 원래대로 왼쪽 구간을 살펴봐야 함
            (2) 원래라면 오른쪽 구간을 살펴봐야 하는 경우: target > nums[mid]
                - 오른쪽 구간(mid ~ hi)이 monotonic 하지만, 그 구간에 속하지 않는다면 왼쪽 구간을 살펴봐야 함
                - 그 외의 경우에는 원래대로 오른쪽 구간을 살펴봐야 함

        이때, 어떤 구간이 monotonic 한지 확인할 때, equal 여부도 함께 확인해야 한다.
            - 왼쪽 구간이 monotonic 하다면 nums[lo] <= nums[mid]
            - 오른쪽 구간이 monotonic 하다면 nums[mid] <= nums[hi]
        """

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # target 발견 시 곧바로 반환
            if nums[mid] == target:
                return mid

            # target이 nums[mid] 보다 작은 경우
            if target < nums[mid]:
                # lo ~ mid 까지 monotonic 하지만, 해당 구간에 속하지 않는다면 오른쪽 살피기
                if nums[lo] <= nums[mid] and target < nums[lo]:
                    lo = mid + 1
                # 그 외의 경우에는 왼쪽 살피기
                else:
                    hi = mid - 1

            # target이 nums[mid] 보다 큰 경우
            else:
                # mid ~ hi 까지 monotonic 하지만, 해당 구간에 속하지 않는다면 왼쪽 살피기
                if nums[mid] <= nums[hi] and target > nums[hi]:
                    hi = mid - 1
                # 그 외의 경우에는 오른쪽 살피기
                else:
                    lo = mid + 1

        return -1
