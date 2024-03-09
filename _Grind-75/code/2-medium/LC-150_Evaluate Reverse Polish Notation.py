# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: x - y),
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: int(x / y))
        }

        stack = []

        for token in tokens:
            if token in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(ops[token](op1, op2))

            else:
                stack.append(int(token))

        return stack[-1]
