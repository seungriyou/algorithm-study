# [LTC] 49 - Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs:
            result["".join(sorted(str))].append(str)
        return list(result.values())

strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
