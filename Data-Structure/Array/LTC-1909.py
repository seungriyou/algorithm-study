# [LTC] 1909 - Remove One Element to Make the Array Strictly Increasing
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed_cnt, prev_num = 0, nums[0]

        for curr_idx in range(1, len(nums)):
            if removed_cnt > 1:
                break

            if nums[curr_idx] <= prev_num:
                removed_cnt += 1
                if curr_idx > 1 and nums[curr_idx] <= nums[curr_idx - 2]:
                    # -- ex) [105, 924(prev_num), 32(X, curr_idx), 968]
                    prev_num = nums[curr_idx - 1]
                    continue
            # -- ex) [1, 2, 10(X), 5(curr_idx, prev_num), 7]
            # -- ex) [100(X), 21(curr_idx, prev_num), 100]
            prev_num = nums[curr_idx]

        return removed_cnt < 2

    def canBeIncreasing2(self, nums: List[int]) -> bool:
        # len(nums) <= 2이면 return True
        if len(nums) <= 2:
            return True

        removed_idx, curr_idx = -1, 1

        while curr_idx < len(nums):
            # nums[curr_idx - 1] < nums[curr_idx] 가 아니라면
            if nums[curr_idx] <= nums[curr_idx - 1]:
                # 기존에 removed 된 내역이 있는 경우, return False
                if removed_idx > -1:
                    return False

                # curr_idx > 1 이고 nums[curr_idx - 2] >= nums[curr_idx] 이면, curr_idx가 removed 되어야 함
                # -- ex) [105(*), 924, 32(curr_idx, removed_idx), 968]
                if curr_idx > 1 and nums[curr_idx] <= nums[curr_idx - 2]:
                    removed_idx = curr_idx

                # 아니라면, curr_idx - 1가 removed 되어야 함
                # -- ex) [1, 2(*), 10(removed_idx), 5(curr_idx), 7]
                # -- ex) [100(removed_idx), 21(curr_idx), 100]
                else:
                    removed_idx = curr_idx - 1

            # nums[curr_idx - 1] < nums[curr_idx]이고, removed_idx가 curr_idx의 바로 왼쪽 옆이라면
            elif removed_idx + 1 == curr_idx:
                # curr_idx - 2와도 비교하여, 이것보다 작거나 같으면 return False
                # -- ex) [541, 783(*), 433(removed_idx), 744(curr_idx)]
                if nums[curr_idx - 2] >= nums[curr_idx]:
                    return False

            curr_idx += 1

        return True


sol = Solution()
nums = [1,2,10,5,7]
print(sol.canBeIncreasing(nums))
print(sol.canBeIncreasing2(nums))