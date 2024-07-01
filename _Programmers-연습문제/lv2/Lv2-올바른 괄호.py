# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []

    for p in s:
        if p == "(":
            stack.append(p)
        elif stack:
            stack.pop()
        else:
            return False

    return len(stack) == 0
