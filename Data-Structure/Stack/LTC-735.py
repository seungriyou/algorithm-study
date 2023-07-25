# [LTC] 735 - Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # -- negative 일 때 left, positive 일 때 right로 이동
        # -- ex) -2  -1   1  2   => -2  -1  1  2
        #        <-  <-  -> ->
        # -- ex) 1  -2  10  -5   => -2  10
        #        -> <-  ->  <-
        # -- ex) 5  10  -2  -5   => 5  10
        #        -> ->  <-  <-

        stack = []

        for a in asteroids:
            remained = True # -- stack에 쌓을지 여부
            # -- 이전 수가 right로, 현재 수가 left로 가야 collide!
            while stack and a < 0 < stack[-1]:
                # -- -a == abs(a)
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                # -- stack[-1] >= abs(a) 인 경우, a는 stack에 쌓지 X
                remained = False
                break
            if remained:
                stack.append(a)

        return stack

sol = Solution()
asteroids = [5,10,-5]
print(sol.asteroidCollision(asteroids))
