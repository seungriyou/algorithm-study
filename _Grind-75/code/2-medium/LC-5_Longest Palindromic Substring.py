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


###### review ######
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """two-pointer (faster)"""

        """
        두 가지 케이스
        (1) substring 길이가 홀수: 가운데 원소는 확인할 필요 x
        (2) substring 길이가 짝수: 모두 확인
        """

        n = len(s)
        res = ""

        # early stop
        if n < 2 or s == s[::-1]:
            return s

        def expand(lo, hi):
            # lo ~ hi - 1의 substring -> 양쪽으로 1씩 늘려가며 제일 긴 palindrome 찾기
            while lo >= 0 and hi <= n and s[lo] == s[hi - 1]:
                lo -= 1
                hi += 1
            return s[lo + 1:hi - 1]

        # 각 위치에서 (1) 홀수 길이 palindrome, (2) 짝수 길이 palindrome의 최댓값 찾기
        for i in range(n):
            res = max(res, expand(i, i + 1), expand(i, i + 2), key=len)

        return res

    def longestPalindrome2(self, s: str) -> str:
        """2D DP (slower)"""

        n = len(s)
        dp = [[False] * n for _ in range(n)]  # dp[lo][hi] = lo ~ hi 까지의 substring이 palindrome 인지 여부
        res = ""

        # early stop
        if n < 2 or s == s[::-1]:
            return s

        """
        세 가지 케이스
        (1) lo == hi: len 1짜리 substring이므로 True
        (2) lo + 1 == hi: len 2짜리 substring이므로, s[lo] == s[hi]
        (3) else: 내부 substring인 s[lo + 1] ~ s[hi - 1]이 palindrom이면서, s[lo] == s[hi]이면 True
            -> dp[lo + 1][hi - 1]을 살펴보아야 하므로, lo는 오른쪽부터 거꾸로 순회해야 함!
        """

        for lo in range(n - 1, -1, -1):  # 오른쪽부터 거꾸로 순회
            for hi in range(lo, n):  # hi는 lo의 오른쪽에 위치해야 함
                if lo == hi:
                    dp[lo][hi] = True

                elif lo + 1 == hi:
                    dp[lo][hi] = s[lo] == s[hi]

                else:
                    dp[lo][hi] = dp[lo + 1][hi - 1] and s[lo] == s[hi]

                if dp[lo][hi] and len(res) < hi - lo + 1:
                    res = s[lo:hi + 1]

        return res
