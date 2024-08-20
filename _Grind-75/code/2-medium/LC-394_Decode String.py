# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # [숫자, [문자]]
        curr_num, curr_str = 0, []

        for c in s:
            # 숫자를 마주치는 경우
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            # 여는 괄호를 마주치는 경우
            elif c == "[":
                stack.append((curr_num, curr_str))
                curr_num, curr_str = 0, []
            # 닫는 괄호를 마주치는 경우
            elif c == "]":
                n, prev_string = stack.pop()
                curr_str = prev_string + n * curr_str
            # 문자를 마주치는 경우
            else:
                curr_str.append(c)

        return "".join(curr_str)
