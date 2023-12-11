# [LTC] 39 - Combination Sum
# https://leetcode.com/problems/combination-sum/

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 중복조합 문제 (DFS, Backtracking)

        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
                # -- 순열 문제로 풀고 싶다면 dfs(..., 0, ...)으로 호출

        dfs(target, 0, [])
        return result

candidates = [2,3,6,7]
target = 7
sol = Solution()
print(sol.combinationSum(candidates, target))
