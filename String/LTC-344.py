# [LTC] 344 - Reverse String
# https://leetcode.com/problems/reverse-string/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # s.reverse()

s = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s)
print(s)
