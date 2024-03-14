# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []

        tmp = []
        tmp_sum = 0

        def backtrack(idx):
            nonlocal tmp_sum

            # tmp_sum이 target을 넘어서면 끊기
            if tmp_sum > target:
                return

            # tmp_sum == target이면 결과 기록하고 끊기
            if tmp_sum == target:
                result.append(tmp[:])
                return

            # 보고 있는 idx의 이전 인덱스의 원소는 볼 필요가 없으므로
            for i in range(idx, n):
                tmp.append(candidates[i])
                tmp_sum += candidates[i]

                backtrack(i)

                tmp.pop()
                tmp_sum -= candidates[i]

        backtrack(0)

        return result
