# [LC] 473 - Matchsticks to Square
# https://leetcode.com/problems/matchsticks-to-square/

from typing import List
from functools import lru_cache


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # === empty bucket(dfs) ===
        # https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/146579/easy-python-28-ms-beats-99-5/

        sum_v = sum(matchsticks)
        n_match = len(matchsticks)

        if sum_v % 4 != 0 or sum_v < 4:
            return False
        side = sum_v // 4

        matchsticks.sort(reverse=True)  # -- for time efficiency
        sides = [0] * 4

        def dfs(i):
            if i == n_match:
                return True
            for j in range(4):
                sides[j] += matchsticks[i]
                if sides[j] <= side and dfs(i + 1):
                    return True
                sides[j] -= matchsticks[i]
                if sides[j] == 0:
                    break
            return False

        return dfs(0)

    def makesquare_dfs(self, matchsticks: List[int]) -> bool:
        # === dfs ===
        sum_v = sum(matchsticks)
        n_match = len(matchsticks)

        if sum_v % 4 != 0 or sum_v < 4:
            return False
        side = sum_v // 4

        matchsticks.sort(reverse=True)  # -- for time efficiency

        @lru_cache(None)
        def dfs(s1, s2, s3, s4, i):
            if s1 > side or s2 > side or s3 > side or s4 > side:
                return False
            if i == n_match:
                return s1 == s2 == s3 == s4 == side

            return dfs(s1 + matchsticks[i], s2, s3, s4, i + 1) \
                   or dfs(s1, s2 + matchsticks[i], s3, s4, i + 1) \
                   or dfs(s1, s2, s3 + matchsticks[i], s4, i + 1) \
                   or dfs(s1, s2, s3, s4 + matchsticks[i], i + 1)

        return dfs(0, 0, 0, 0, 0)

matchsticks = [3,3,3,3,4]
sol = Solution()
print(sol.makesquare_dfs(matchsticks))
