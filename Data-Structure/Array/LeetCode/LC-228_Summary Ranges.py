# https://leetcode.com/problems/summary-ranges/

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []  # [[range_start, range_end], ...]
        for n in nums:
            if result and result[-1][1] + 1 == n:
                result[-1][1] += 1
            else:
                result.append([n, n])

        return [f"{s}->{e}" if s != e else str(s) for s, e in result]

    def summaryRanges2(self, nums: List[int]) -> List[str]:
        result = []
        start = 0

        for i in range(len(nums)):
            # 다음 원소가 존재하고, 현재 원소와 다음 원소의 차이가 1일 때는 넘어가기
            if i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                continue
            # 아니라면, start ~ 현재 원소까지의 range 추가하고, start를 다음 원소로 갱신하기
            else:
                if start == i:
                    result.append(str(nums[i]))
                else:
                    result.append(f"{nums[start]}->{nums[i]}")
                start = i + 1

        return result

nums = [0,2,3,4,6,8,9]
sol = Solution()
print(sol.summaryRanges(nums))
