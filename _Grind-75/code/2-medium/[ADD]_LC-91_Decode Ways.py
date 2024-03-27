# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings1(self, s: str) -> int:
        """
        [ O(1) DP ]
        1D DP에서, 이전 값과 그 이전의 값만 확인하므로 O(1)으로 최적화 가능
        """

        # base condition
        prev2, prev1 = 1, 0 if s[0] == "0" else 1

        for i in range(1, len(s)):
            tmp = 0

            # 1-step
            if 1 <= int(s[i]) <= 9:
                tmp += prev1

            # 2-step
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                tmp += prev2

            prev2, prev1 = prev1, tmp

        return prev1

    def numDecodings(self, s: str) -> int:
        """
        [ 1D DP ]
        dp: (len(s) + 1) 길이의 리스트
        dp[i]: i번째 숫자를 보고있을 때, 여기까지 decode 가능한 경우의 수

        decode 가능한 값의 범위가 1 ~ 26이므로, decode 가능한 경우는 다음과 같이 두 가지이다.
            - 현재 보고 있는 숫자 하나 (= s[i - 1]): 1 ~ 9 이내
            - 현재 보고 있는 숫자와 이전 것 두개 (= s[i - 2:i]): 10 ~ 26 이내

        따라서, 각 단계마다 현재 보고 있는 숫자 값에 따라서 1-step 전인 dp[i - 1]와 2-step 전인 dp[i - 2]를 이용해야 한다.
        """

        n = len(s) + 1
        dp = [0] * n

        # base condition
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, n):
            # 1-step 전
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]

            # 2-step 전
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n - 1]
