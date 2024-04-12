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


###### review ######
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for p in s:
            # 여는 괄호: stack에 넣기
            if p not in matching:
                stack.append(p)

            # 닫는 괄호: (1) stack이 비어있거나 (2) top과 짝이 맞지 않으면 종료
            elif not stack or stack.pop() != matching[p]:
                return False

            # top과 짝이 맞으면 상쇄 후 넘어가기! (이미 pop() 했으므로 넘어가기)

        return len(stack) == 0

    def isValid1(self, s: str) -> bool:
        stack = []

        matching = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for p in s:
            # 여는 괄호
            if p not in matching:
                stack.append(p)

            # 닫는 괄호
            # (1) top과 짝이 맞으면 상쇄
            elif stack and stack.pop() == matching[p]:
                continue
            # (2) stack이 비어있거나 top과 짝이 맞지 않으면 빠르게 종료
            else:
                return False

        return len(stack) == 0
