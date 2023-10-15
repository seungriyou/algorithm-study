# [LC] 698 - Partition to K Equal Sum Subsets
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_s = sum(nums)
        nums_l = len(nums)
        if nums_s % k != 0 or nums_s < k:
            return False

        sum_l = [0] * k
        sub_sum = nums_s // k
        nums.sort(reverse=True)

        def dfs(i):
            if i == nums_l:
                return True
            for j in range(k):
                sum_l[j] += nums[i]
                if sum_l[j] <= sub_sum and dfs(i + 1):
                    return True
                sum_l[j] -= nums[i]
                if sum_l[j] == 0:  # -- empty bucket에도 들어갈 수 없으면 다른 bucket 탐색 안 해봐도 ok
                    break
            return False

        return dfs(0)

nums = [4,3,2,3,5,2,1]
k = 4
sol = Solution()
print(sol.canPartitionKSubsets(nums, k))
