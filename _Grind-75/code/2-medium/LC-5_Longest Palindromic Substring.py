# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        [ Two pointer ]
        - palindrome의 두 가지 종류
            (1) 길이가 홀수: 가운데 문자는 확인하지 않아도 ok
            (2) 길이가 짝수: 전부 확인
        """

        n = len(s)
        if n < 2 or s == s[::-1]:
            return s

        def expand(left, right):
            """left, right를 양끝으로 늘려가며 palindrome을 찾는 함수"""
            while left >= 0 and right <= n and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        result = ""
        for i in range(n):
            result = max(
                result,
                expand(i, i + 1),  # 홀수 길이 palindrome 찾기
                expand(i, i + 2),  # 짝수 길이 palindrome 찾기
                key=len
            )

        return result

    def longestPalindrome_dp(self, s: str) -> str:
        """
        [ 2D DP ]
        - dp[lo][hi]: lo번째 문자 ~ hi번째 문자까지 palindrome 인지 여부
        - 케이스 나누기
            (1) lo == hi일 때: dp[lo][hi] = True
                -> 문자 하나로 이루어진 substring 이므로

            (2) hi == lo + 1일 때: dp[lo][hi] = s[lo] == s[hi]
                -> 문자 두 개로 이루어진 substring 이므로

            (3) 그 외: dp[lo][hi] = dp[lo + 1][hi - 1] and (s[lo] == s[hi])
                -> 내부가 palindrome 인지 && 양 끝의 두 문자가 같은지
                -> `lo + 1`을 살펴보아야 하므로, lo는 오른쪽부터 순회해야 함
        """

        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        result = ""

        for lo in range(n - 1, -1, -1):  # lo는 오른쪽부터 순회
            for hi in range(lo, n):  # hi는 lo에서 출발해야 함
                # (1) lo == hi일 때: dp[lo][hi] = True
                if lo == hi:
                    dp[lo][hi] = True

                # (2) hi == lo + 1일 때: dp[lo][hi] = s[lo] == s[hi]
                elif hi == lo + 1:
                    dp[lo][hi] = s[lo] == s[hi]

                # (3) 그 외: dp[lo][hi] = dp[lo + 1][hi - 1] and (s[lo] == s[hi])
                else:
                    dp[lo][hi] = dp[lo + 1][hi - 1] and (s[lo] == s[hi])

                # tracking the longest palindrome
                if dp[lo][hi] and len(result) < hi - lo + 1:
                    result = s[lo:hi + 1]

        return result
