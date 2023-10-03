# [PG] 12909 - 올바른 괄호 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:  # -- i == ')'
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

    return False if stack else True

s = "(())()"
assert True == solution(s)
