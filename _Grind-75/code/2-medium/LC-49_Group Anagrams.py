# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        tmp = defaultdict(list)

        for s in strs:
            tmp["".join(sorted(s))].append(s)

        return list(tmp.values())
