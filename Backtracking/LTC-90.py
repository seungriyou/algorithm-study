# [LTC] 90 - Subsets II
# https://leetcode.com/problems/subsets-ii/

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        nums = [1, 2, 2] 일 때, 트리는 다음과 같다.
        (X는 같은 레벨에서 중복을 피하여 continue 한 경우)
            1      2     X
           / \    /
          2   X  2
         /
        2
        -> dfs backtracking
        """
        result = []
        nums.sort() # -- 정렬 시 순차적으로 순회하면서 중복 값을 건너뛸 수 있음

        def dfs(idx: int, path: List[int]) -> None:
            result.append(path)

            for i in range(idx, len(nums)):
                # -- 같은 레벨(= 형제 노드) 내에서만 중복을 피하면 되므로
                # -- (1) 해당 레벨의 첫 번째(i == idx인 경우)로 등장하는 수가 아니면서
                # -- (2) (nums가 정렬되어 있으므로) 직전의 수와 비교했을 때 같으면
                # -- continue로 넘어감
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        return result

sol = Solution()
# nums = [1,2,2]
nums = [0]
print(sol.subsetsWithDup(nums))
