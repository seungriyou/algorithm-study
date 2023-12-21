# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/
# https://app.codility.com/demo/results/training6YDRAF-742/

def solution(S):
    stack = []

    for s in S:
        if s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                continue

        stack.append(s)

    return int(len(stack) == 0)
