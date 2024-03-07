# https://leetcode.com/problems/valid-palindrome/

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. uppercase -> lowercase
        s = s.lower()

        # 2. remove non-alphanumeric (only letters, numbers)
        s = re.sub("[^a-z0-9]", "", s)

        return s == s[::-1]
