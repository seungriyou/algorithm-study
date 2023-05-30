# [LTC] 125 - Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # uppercase -> lowercase
        s = s.lower()
        # remove all non-alphanumeric characters
        s = re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]

s = "0P"
solution = Solution()
print(solution.isPalindrome(s))
