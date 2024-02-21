# https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    stack = []

    for n in number:
        while k and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    if k:
        stack = stack[:-k]

    return ''.join(stack)
