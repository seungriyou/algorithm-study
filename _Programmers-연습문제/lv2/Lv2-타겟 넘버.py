# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    def dfs(idx, val):
        nonlocal answer

        # base condition
        if idx == len(numbers):
            answer += target == val
            return

        # recur
        dfs(idx + 1, val - numbers[idx])
        dfs(idx + 1, val + numbers[idx])

    dfs(0, 0)

    return answer
