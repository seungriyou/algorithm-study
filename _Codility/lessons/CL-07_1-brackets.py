# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
# https://app.codility.com/demo/results/trainingYF726V-RJZ/

def solution(S):
    matching = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    stack = []

    for s in S:
        # 여는 괄호일 때
        if s not in matching:
            stack.append(s)
        # 닫는 괄호일 때
        else:
            # stack이 비어있거나, stack의 top이 matching 되는 괄호가 아닌 경우, 빠르게 return 0
            if not stack or stack.pop() != matching[s]:
                return 0

    return 1 if not stack else 0
