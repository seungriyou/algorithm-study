# [PG] 43165 - 타겟넘버 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution_dfs(numbers, target):
    answer = 0

    def dfs(idx, val):
        nonlocal answer

        if idx == len(numbers):
            if val == target:
                answer += 1
            return

        dfs(idx + 1, val + numbers[idx])
        dfs(idx + 1, val - numbers[idx])

    dfs(0, 0)

    return answer

# =======================

from collections import deque

def solution_bfs(numbers, target):
    answer = 0
    q = deque([numbers[0], -numbers[0]])

    for i in range(1, len(numbers)):
        # level = len(q)
        # for _ in range(level):
        for _ in range(len(q)):
            v = q.popleft()
            q.append(v + numbers[i])
            q.append(v - numbers[i])

    for leaf in q:
        if leaf == target:
            answer += 1

    return answer

# =======================

from itertools import product

def solution(numbers, target):
    pairs = [(n, -n) for n in numbers]
    return list(map(sum, product(*pairs))).count(target)


numbers = [4, 1, 2, 1]
target = 4
assert 2 == solution(numbers, target) == solution_bfs(numbers, target) == solution_dfs(numbers, target)
