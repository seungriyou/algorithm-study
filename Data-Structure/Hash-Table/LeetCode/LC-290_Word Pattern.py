# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ntop, pton = {}, {}
        names = s.split()

        if len(pattern) != len(names):
            return False

        for p, name in zip(pattern, names):
            if name in ntop and ntop[name] != p:
                return False
            if p in pton and pton[p] != name:
                return False

            ntop[name] = p
            pton[p] = name

        return True

sol = Solution()
pattern = "abba"
s = "dog cat cat fish"
print(sol.wordPattern(pattern, s))
