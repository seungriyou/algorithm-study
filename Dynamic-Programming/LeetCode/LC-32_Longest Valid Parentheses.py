# [LTC] 32 - Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # === DP ===
        n = len(s)
        max_len = 0
        dp = [0] * n

        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                else:
                    p = i - dp[i - 1] - 1
                    if p >= 0 and s[p] == "(":
                        dp[i] = 2 + dp[i - 1] + (dp[p - 1] if p - 1 >= 0 else 0)
            max_len = max(max_len, dp[i])

        return max_len

    def longestValidParentheses_dp1(self, s: str) -> int:
        # === DP ===
        # -- dp[i]: i번째 문자까지의 substring 내의 longest valid parentheses
        # -- p: 현재 문자가 ")"일 때, 이와 match 되는 "("의 idx 일 수 있는 값

        n = len(s)
        max_len = 0
        dp = [0] * n

        for i in range(1, n):
            p = i - dp[i - 1] - 1
            if p >= 0 and s[i] == ")" and s[p] == "(":
                dp[i] = dp[p - 1] + dp[i - 1] + 2  # -- p 이전 까지의 값 + i 이전 까지의 값 + 현재 세고 있는 "()" 쌍
                max_len = max(max_len, dp[i])

        return max_len

    def longestValidParentheses_1(self, s: str) -> int:
        # === Stack 1 ===
        """
        ()(())
        0   (   push    [-1, 0]
        1   )   pop     [-1]        1 - (-1) = 2
        2   (   push    [-1, 2]
        3   (   push    [-1, 2, 3]
        4   )   pop     [-1, 2]     4 - 2 = 2
        5   )   pop     [-1]        5 - (-1) = 6

        ())()
        0   (   push    [-1, 0]
        1   )   pop     [-1]        1 - (-1) = 2
        2   )   pop     [2]         * valid parentheses가 존재할 수 있는 시작 위치 update
        3   (   push    [2, 3]
        4   )   pop     [2]         4 - 2 = 2
        """
        stack = [-1]  # -- valid parentheses가 존재할 수 있는 시작 위치의 바로 왼쪽 index
        max_len = 0

        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:  # -- valid parentheses가 존재할 수 있는 시작 위치 update (이전 범위에서는 더이상 valid p 찾을 수 X)
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

    def longestValidParentheses_2(self, s: str) -> int:
        # === Stack 2 ===
        """
        ()(())
        0   (   push    [-1, 0]
        1   )   pop     [-1]        1 - (-1) = 2
        2   (   push    [-1, 2]
        3   (   push    [-1, 2, 3]
        4   )   pop     [-1, 2]     4 - 2 = 2
        5   )   pop     [-1]        5 - (-1) = 6

        ())()
        0   (   push    [-1, 0]
        1   )   pop     [-1]        1 - (-1) = 2
        2   )   push    [-1, 2]
        3   (   push    [-1, 2, 3]
        4   )   pop     [-1, 2]     4 - 2 = 2
        """
        stack = [-1]  # -- valid parentheses가 존재할 수 있는 시작 위치의 바로 왼쪽 index
        max_len = 0

        for i, p in enumerate(s):
            if stack[-1] != -1 and p == ")" and s[stack[-1]] == "(":
                stack.pop()
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)

        return max_len

sol = Solution()
s = ")()())"
print(sol.longestValidParentheses(s))
