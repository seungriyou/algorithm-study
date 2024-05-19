# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """0/1 knapsack - 1D DP
            2D DP에서 이전 row(dp[i - 1])의 값(dp[i - 1][j] 혹은 dp[i - 1][j - nums[i - 1]])만 필요했으므로,
            1D DP로 space-optimize 가능!
            단, dp[i - 1]의 [j] 혹은 [j - nums[i - 1]]와 같이 이전 인덱스를 확인해야하므로, 오른쪽 -> 왼쪽 순으로 순회해야 한다.
        """

        total = sum(nums)
        n = len(nums)

        # 총합이 홀수라면 false
        if total & 1:
            return False

        target = total // 2

        # dp[j] = nums의 i번째 원소까지 봤을 때, 그 합이 j인 조합이 존재하는지 여부
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:  # -- 값 (배낭에 넣을 물건)
            for j in range(target, num - 1, -1):  # -- 합 (배낭의 임시 용량): 현재 넣으려는 물건 무게의 이상인 값만 보면 된다!
                dp[j] = dp[j] or dp[j - num]
            # for j in range(target, 0, -1):
            #     if j >= num:
            #         dp[j] |= dp[j - num]

        return dp[target]

    def canPartition1(self, nums: List[int]) -> bool:
        """0/1 knapsack - 2D DP"""

        total = sum(nums)
        n = len(nums)

        # 총합이 홀수라면 false
        if total & 1:
            return False

        target = total // 2

        # dp[i][j] = nums의 i번째 원소까지 봤을 때, 그 합이 j인 조합이 존재하는지 여부
        # j == 0: 합이 0인 조합은 모든 물건에서 가능하다! (안 넣으면 됨)
        dp = [[True] + [False] * target for _ in range(n + 1)]

        for i in range(1, n + 1):  # -- 값 (배낭에 넣을 물건)
            for j in range(1, target + 1):  # -- 합 (배낭의 임시 용량)
                # i번째 물건(= nums[i - 1])이 배낭의 임시 용량 j보다 같거나 작다면, i번째 물건을 아예 넣을 수 없으므로 i-1번째 물건까지 살펴본 값을 넣음
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                # 그렇지 않다면, i번째 물건을 넣지 않는 경우와 넣는 경우 중 하나라도 가능한지 확인
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][target]
