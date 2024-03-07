# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for p in s:
            # 여는 괄호이면 stack에 넣기
            if p not in matching:
                stack.append(p)

            # 닫는 괄호이면 (1) stack이 비어있거나, (2) stack의 top이 대응되는 여는 괄호가 아니라면 빠르게 False 반환
            elif not stack or matching[p] != stack.pop():
                return False

        # s가 valid 했다면 stack에 남아있는 괄호가 없어야 함
        return len(stack) == 0
