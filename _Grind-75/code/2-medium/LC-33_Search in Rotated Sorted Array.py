# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # nums[mid] < nums[right]이면, mid 기준 오른쪽(mid ~ right)이 정렬됨
            if nums[mid] < nums[right]:
                # 정렬된 구간인 오른쪽에 target이 위치한다면, 오른쪽 보기
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            # 아니라면, mid 기준 왼쪽(left ~ mid)이 정렬됨
            else:
                # 정렬된 구간인 왼쪽에 target이 위치한다면, 왼쪽 보기
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


###### review ######
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 발견했으면 반환
            if nums[mid] == target:
                return mid

            # mid ~ right 까지 정렬되어 있는 경우
            if nums[mid] < nums[right]:
                # 정렬된 곳에 target이 속하면, 그 부분으로 이동 (등호 주의!)
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # 아니라면, 다른 부분으로 이동
                else:
                    right = mid - 1

            # left ~ mid 까지 정렬되어 있는 경우
            else:
                # 정렬된 곳에 target이 속하면, 그 부분으로 이동
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # 아니라면, 다른 부분으로 이동
                else:
                    left = mid + 1

        return -1
