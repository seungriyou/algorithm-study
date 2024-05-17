# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea1(self, height: List[int]) -> int:
        """양끝에서 시작하는 two pointer"""

        left, right = 0, len(height) - 1
        water = 0

        while left < right:
            # water 업데이트
            water = max(water, (right - left) * min(height[left], height[right]))

            # height가 작은 쪽의 pointer를 안쪽으로 움직이기
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return water

    def maxArea(self, height: List[int]) -> int:
        """양끝에서 시작하는 two pointer"""

        left, right = 0, len(height) - 1
        water = 0

        while left < right:
            # water 업데이트
            water = max(water, (right - left) * min(height[left], height[right]))

            # height가 작은 쪽의 pointer를 안쪽으로 움직이기
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            # 양쪽의 height가 동일하다면, 하나의 pointer만 이동한다고 해서 현재의 water보다 큰 값을 찾을 수 없으므로
            # 두 pointer 모두 이동하기
            else:
                left += 1
                right -= 1

        return water
