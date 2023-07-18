# [LTC] 416 - Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot_sum = sum(nums)

        # -- 합이 동일한 2 subsets로 나누어야하므로 총합이 홀수이면 false
        if tot_sum % 2 == 1:
            return False

        # -- 총합이 짝수라면, 2로 나눈 값을 subset의 총합으로 설정
        sub_sum = tot_sum // 2

        # -- dp 리스트: 원소들을 더해서 각 인덱스의 값을 만들 수 있는지 여부 저장
        dp = [False] * (sub_sum + 1)
        dp[0] = True

        # -- nums의 각 원소 순회
        for n in nums:
            # -- n 이상의 인덱스들에 대해서만 확인
            # -- (합을 확인하기위해 더 작은 인덱스의 값을 확인해야 함 -> 거꾸로 순회해야 함)
            for i in range(sub_sum, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]
        return dp[sub_sum]

sol = Solution()
nums = [1,5,11,5]
# nums = [1,2,3,5]
print(sol.canPartition(nums))
