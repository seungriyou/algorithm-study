# [LTC] 150 - Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_mapping = {
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
            "*": (lambda a, b: a * b),
            "/": (lambda a, b: int(a / b))
        }

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                stack.append(op_mapping[token](a, b))

            else:
                stack.append(int(token))

        return stack[0]

tokens = ["2","1","+","3","*"]
sol = Solution()
print(sol.evalRPN(tokens))
