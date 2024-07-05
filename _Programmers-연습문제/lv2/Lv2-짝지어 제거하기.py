# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []

    for _s in s:
        if stack and stack[-1] == _s:
            stack.pop()
        else:
            stack.append(_s)

    return 0 if stack else 1
