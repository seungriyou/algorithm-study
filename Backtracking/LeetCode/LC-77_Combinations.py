# [LTC] 77 - Combinations
# https://leetcode.com/problems/combinations/

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            # -- 종료 조건
            if k == 0:
                results.append(elements[:]) # -- 복사하기

            # -- 반복하기
            for i in range(start, n + 1):   # -- 전체 숫자 [1, n] 순회
                elements.append(i)
                dfs(elements, i + 1, k - 1) # -- i + 1: 이전 선택한 숫자와 겹치지 X (k회 deeper)
                elements.pop()

        dfs([], 1, k)
        return results

sol = Solution()
n = 4
k = 2
print(sol.combine(n=4, k=2))
