# [BOJ] 11578 - 팀원 모집

import sys
import itertools
from typing import List
sys.stdin = open('input.txt')
input = sys.stdin.readline


def min_student(N: int, M: int, problems: List[int]) -> int:
    # 1명이 모든 문제를 풀 수 있는 경우
    if 2 ** N - 1 in problems:
        return 1
    # m명이 모든 문제를 풀 수 있는 경우
    for m in range(2, M + 1):
        for comb in itertools.combinations(problems, m):
            result = 0
            for c in comb:
                result |= c
            if result == 2 ** N - 1:
                return m
    # 모든 학생이 풀어도 모든 문제를 풀 수 없는 경우
    return -1


N, M = map(int, input().split())
problems = []

for _ in range(M):
    student = list(map(int, input().split()))[1:]
    problem = 0
    for i in student:
        problem += 2 ** (i - 1)
    problems.append(problem)

print(min_student(N, M, problems))
