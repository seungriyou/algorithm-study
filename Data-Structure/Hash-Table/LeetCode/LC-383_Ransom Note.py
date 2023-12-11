# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for note in ransomNote:
            if counter[note] > 0:
                counter[note] -= 1
            else:
                return False

        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1, cnt2 = Counter(ransomNote), Counter(magazine)

        return cnt1 & cnt2 == cnt1


ransomNote = "aa"
magazine = "ab"
sol = Solution()
print(sol.canConstruct(ransomNote, magazine))
print(sol.canConstruct2(ransomNote, magazine))
