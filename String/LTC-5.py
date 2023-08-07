# [LTC] 5 - Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        result = ""
        for i in range(len(s) - 1):
            result = max(
                result,
                expand(i, i + 1),   # -- 짝수 길이 palindrome
                expand(i, i + 2),   # -- 홀수 길이 palindrome
                key=len
            )

        return result


sol = Solution()
s = "cbbd"
print(sol.longestPalindrome(s))
