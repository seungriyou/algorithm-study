# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0

        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == n

sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))
