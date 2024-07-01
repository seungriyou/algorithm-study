# https://school.programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = [0]     # 현재 보고있는 curr_idx가 가리키는 price보다 작거나 같은 price의 idx를 가지고 있어야 한다!

    for curr_idx in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[curr_idx]:
            higher_idx = stack.pop()
            answer[higher_idx] = curr_idx - higher_idx
        stack.append(curr_idx)

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))     # should print 	[4, 3, 1, 1, 0]


##### review #####
def solution(prices):
    n = len(prices)

    answer = [n - i - 1 for i in range(n)]
    stack = []

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer
