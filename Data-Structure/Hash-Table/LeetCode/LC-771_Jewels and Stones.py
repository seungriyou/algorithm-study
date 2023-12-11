# [LTC] 771 - Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # sol 1
        jewels_cnt = {j: 0 for j in jewels}
        for s in stones:
            if s in jewels_cnt:
                jewels_cnt[s] += 1
        return sum(jewels_cnt.values())

        # sol 2
        # return sum([s in jewels for s in stones])

jewels = "z"
stones = "ZZ"

sol = Solution()
print(sol.numJewelsInStones(jewels, stones))
