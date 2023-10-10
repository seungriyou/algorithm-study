# [LC] 229 - Majority Element II
# https://leetcode.com/problems/majority-element-ii/

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # === boyer-moore majority vote algorithm (O(n) time & O(1) space) ===
        # floor(n/3) 보다 많이 등장할 수 있는 숫자의 개수는 최대 2개이다!
        # 그 두 숫자가 될 수 있는 숫자를 cand1, cand2라고 하고, 각각에 대해 cnt 값을 가져나간다.

        cnt1 = cnt2 = cand1 = 0
        cand2 = 1

        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        result = []
        if nums.count(cand1) > len(nums) // 3:
            result.append(cand1)
        if nums.count(cand2) > len(nums) // 3:
            result.append(cand2)
        return result

        # return [cand for cand in (cand1, cand2) if nums.count(cand) > len(nums) // 3]

sol = Solution()
nums = [3,2,3]
print(sol.majorityElement(nums))
