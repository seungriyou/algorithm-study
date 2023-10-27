# [BJ] 15650 - N과 M (2)
# https://www.acmicpc.net/problem/15650

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

elements = list(range(1, n + 1))
prev_elements = []

def backtrack(idx):
    # base case
    if len(prev_elements) == m:
        print(' '.join(map(str, prev_elements)))
        return

    for i in range(idx, n):
        prev_elements.append(elements[i])
        backtrack(i + 1)
        prev_elements.pop()

backtrack(0)

# def backtrack(idx, path):
#     # base case
#     if len(path) == m:
#         print(path)
#         return
#
#     for i in range(idx, n):
#         backtrack(i + 1, path + [elements[i]])
#
# backtrack(0, [])
