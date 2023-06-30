# [LTC] 20 - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for p in s:
            if p not in matching:
                stack.append(p)
            elif not stack or matching[p] != stack.pop():
                return False

        return len(stack) == 0

sol = Solution()
s = "("
print(sol.isValid(s))