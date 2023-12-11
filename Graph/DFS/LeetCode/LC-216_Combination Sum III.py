# [LC] 216 - Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def dfs(cn, ck, idx, path):
            # cn: n에서부터 선택된 숫자를 뺌
            # ck: k에서부터 숫자가 선택될 때마다 1씩 감소
            if ck < 0 or cn < 0:
                return
            if cn == 0 and ck == 0:
                result.append(path)
                return
            for i in range(idx, 10):    # i = idx ~ 9까지의 숫자
                dfs(cn - i, ck - 1, i + 1, path + [i])  # at most once 이므로 idx는 다음 idx인 i + 1 건네주기

        dfs(n, k, 1, [])
        return result

k = 3
n = 9
sol = Solution()
print(sol.combinationSum3(k, n))
