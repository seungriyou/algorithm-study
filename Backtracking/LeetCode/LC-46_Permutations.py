# [LTC] 46 - Permutations
# https://leetcode.com/problems/permutations/

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 백트래킹
        prev_elements = []
        result = []

        def dfs(elements):
            # 종료 조건 (리프 노드일 때, result에 추가)
            if len(elements) == 0:
                result.append(prev_elements[:]) # -- 복사해서 넣기

            # element 내 원소 반복
            for e in elements:
                # 다음에 올 수 있는 elements
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e) # -- stack 처럼 사용
                dfs(next_elements) # -- next_elements에 대해 dfs 계속 수행
                prev_elements.pop()

        dfs(nums)
        return result

sol = Solution()
nums = [1,2,3]
print(sol.permute(nums))
