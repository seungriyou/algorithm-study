# https://leetcode.com/problems/asteroid-collision/

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # collide가 발생 가능한 경우 동안 반복
            while stack and a < 0 < stack[-1]:
                # <1> a의 size가 더 큰 경우에는 반복해서 stack.pop()
                if stack[-1] < -a:
                    stack.pop()
                    continue
                # <2> stack[-1]의 size가 더 큰 경우에는 a 제외
                elif stack[-1] > -a:
                    break
                # <3> a의 size와 stack[-1]의 size가 동일하다면 stack[-1] & a 둘다 제외
                else:
                    stack.pop()
                    break
            # <1>의 경우에 해당한다면 stack에 a 추가
            else:
                stack.append(a)

        return stack

    def asteroidCollision1(self, asteroids: List[int]) -> List[int]:
        """
        stack 활용
        매 단계에서 collide가 발생 가능한 경우는 stack[-1]이 오른쪽으로(positive),
        현재 asteroid가 왼쪽으로(negative) 이동하는 경우이다.
        """

        stack = []
        for a in asteroids:
            remained = True

            # collide가 발생 가능한 경우 동안 반복
            while stack and a < 0 < stack[-1]:
                # a의 size가 더 큰 경우에는 반복해서 stack.pop()
                if stack[-1] < -a:
                    stack.pop()
                    continue
                # a의 size와 stack[-1]의 size가 동일하다면 stack[-1] & a 둘다 제외
                elif stack[-1] == -a:
                    stack.pop()
                # 현재의 a가 stack에 저장되지 않는 경우에는 빠르게 break
                remained = False
                break

            if remained:
                stack.append(a)

        return stack
