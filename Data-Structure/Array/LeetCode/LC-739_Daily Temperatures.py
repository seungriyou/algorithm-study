# [LTC] 739 - Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        answer = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer

temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures((temperatures)))
