# [LTC] 15 - 3Sum
# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # -- 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # -- 간격 줄여나가면서 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # -- sum == 0
                    result.append([nums[i], nums[left], nums[right]])
                    # -- 다음 값과 중복인 경우를 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result

sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))
