# [LTC] 10 - Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] = s[:i]가 p[:j]과 대응되는지 여부 (즉, s[i-1]와 p[j-1]를 봐야함)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # -- s와 p가 모두 ""일 때 = True
        dp[0][0] = True

        # -- p가 ""일 때, s[:i]에서 i==0일 때를 제외하고는 모두 False여야 하므로 그대로 둠

        # -- s가 ""일 때, (1) p도 "" 이거나 (2) "*"가 존재해야 함 (0번 등장해도 ok)
        for j in range(2, len(p) + 1):
            dp[0][j] = p[j - 1] == "*" and dp[0][j - 2] # -- "*" 등장 전전까지의 state 반영

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # -- p에서 "*"를 만난 경우
                if p[j - 1] == "*":
                    # 둘 중 하나라도 True이면 True
                    # -- (1) p에서 "*" 등장 전전까지의 state (0번 등장해도 ok)
                    # -- (2) "*" 앞의 문자가 "."이거나 s와 동일한 문자인 경우, s에서 이전 문자까지의 state
                    # dp[i][j] = dp[i][j - 2] or ((p[j - 2] in {".", s[i - 1]}) and dp[i - 1][j])
                    dp[i][j] = dp[i][j - 2] or ((p[j - 2] == "." or p[j - 2] == s[i - 1]) and dp[i - 1][j])
                # -- p에서 "."를 만났거나 s와 동일한 문자를 만난 경우, 이전 state 반영
                else:
                    # dp[i][j] = (p[j - 1] in {".", s[i - 1]}) and dp[i - 1][j - 1]
                    dp[i][j] = (p[j - 1] == "." or p[j - 1] == s[i - 1]) and dp[i - 1][j - 1]

        return dp[-1][-1]

sol = Solution()
s = "aa"
p = "a*"
print(sol.isMatch(s, p))
