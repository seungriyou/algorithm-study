# [LTC] 42 - Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        volume_at_i: slot i에서 trap 가능한 water의 volume
                  __
                 |
               __| ..... right_max[i]: slot i에서 right side의 height로 가능한 가장 큰 값
         __ ,,| ........ left_max[i] : slot i에서 left side의 height로 가능한 가장 큰 값
           |  |
           |__| ........ height[i]   : slot i의 height
         __,__,__,__ ... 0
         i-1 i i+1

        => volume_at_i = min(left_max[i], right_max[i]) - height[i] (if > 0)
        """

        l = len(height)
        if l < 3:
            return 0

        left_max, right_max = [0] * l, [0] * l
        left_max[0], right_max[-1] = 0, 0
        volume = 0

        for i in range(1, l):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        for i in range(l - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])

        for i in range(l):
            if (volume_at_i := min(left_max[i], right_max[i]) - height[i]) > 0:
                volume += volume_at_i

        return volume

    def trap_2p(self, height: List[int]) -> int:
        # === two pointer ===
        l = len(height)
        if l < 3:
            return 0

        left, right = 0, l - 1
        left_max, right_max = height[left], height[right]
        volume = 0

        # left와 right가 height가 가장 높은 지점에서 만나도록 한다.
        # height가 가장 높은 곳을 중심으로 나누면,
        # 왼쪽에서는 -->, 오른쪽에서는 <-- 방향으로 이동하며
        # 각각 현재 위치까지의 max 값에서 현재 height를 뺀 값이 해당 slot에서 저장 가능한 물의 양이다.
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

    def trap_stack(self, height: List[int]) -> int:
        # === stack ===
        volume = 0
        stack = []  # -- idx

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                height_diff = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * height_diff

            stack.append(i)

        return volume

height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap_2p(height))
