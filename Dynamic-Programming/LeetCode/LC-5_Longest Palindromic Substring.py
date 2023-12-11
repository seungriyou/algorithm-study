# [LTC] 5 - Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        dp = [[-1] * (len_s) for _ in range(len_s)]
        result = ""
        for l in range(len_s, -1, -1):      # -- 거꾸로 가야 dp[l + 1][h - 1] 참조 가능
            for h in range(l, len_s):   # -- h는 무조건 l보다 같거나 큼!!
                # (1) l == h: 대각선에 위치 -> 자기 자신이므로 True
                if l == h:
                    dp[l][h] = True
                # (2) h == l + 1: len 2짜리 substring이므로, 문자가 같은지 여부
                elif l == l + 1:
                    dp[l][h] = s[l] == s[h]
                # (3) h > l + 1: 현재 문자가 같은지 여부 && 내부 substring의 값
                else:
                    dp[l][h] = dp[l + 1][h - 1] and s[l] == s[h]
                # track max length palindrome substring
                if dp[l][h] and h - l + 1 > len(result):
                    result = s[l:h + 1]

        return result

sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))
