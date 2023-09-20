# [LC] 44 - Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/

class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        # === 1-D dp로 줄인 것 ===
        """
        if p[j] == '*':
            dp[i][j] = f(i - 1, j) or f(i, j - 1)
        if p[j] == '?':
            dp[i][j] = f(i - 1, j - 1)
        if p[j] not *, ?:
            dp[i][j] = f(i - 1, j - 1) if s[i] == p[j] else False

        dp[j] = before the write operation refers to dp[i - 1][j]
        dp[j - 1] = refers to dp[i][j - 1]
        dp[i - 1][j - 1] = prev_diag
        * * * * * *
        * * * * * *
        """
        dp = [False for _ in range(len(p) + 1)]
        if not s and not p:
            return True
        j = 1
        while j < len(p) + 1 and p[j - 1] == '*':
            dp[j] = True
            j += 1

        for i in range(1, len(s) + 1):
            prev_diag = i == 1  # True only when dp[0][0]
            for j in range(1, len(p) + 1):
                prev_row = dp[j]
                if p[j - 1] == '*':
                    dp[j] = dp[j] or dp[j - 1]  # dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[j] = prev_diag and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
                prev_diag = prev_row

        return dp[-1]

    def isMatch_2d(self, s: str, p: str) -> bool:
        # 참고: https://leetcode.com/problems/regular-expression-matching/

        # dp[i][j]: s[:i]와 p[:j]가 match 되는지 여부 (s[i - 1], p[j - 1]을 봐야함)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # s = "", p = "" 일 때, True
        dp[0][0] = True

        # p = "" 일 때, s = "" 일 때 제외하고는 False이므로 그대로 두기

        # s = "" 일 때, (1) p = "" 이거나 (2) "*"가 존재해야 함
        # 이때, "*"가 연달아나오지 않으면 break
        for j in range(1, len(p) + 1):
            if p[j - 1] != '*':
                break
            dp[0][j] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # -- 현재 보는 p가 '*'인 경우
                if p[j - 1] == '*':
                    # 둘 중 하나가 True 라면 True
                    # -- (1) 이전 s까지의 state
                    # -- (2) 이전 p까지의 state
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

                # -- 현재 보는 p가 '?'이거나 현재 보는 s와 같은 경우, 이전 state 반영
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == '?' or p[j - 1] == s[i - 1])
                # elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                #     dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]

s = "cb"
p = "?a"
sol = Solution()
print(sol.isMatch(s, p))
