# [BJ] 15652 - N과 M (4)
# https://www.acmicpc.net/problem/15652

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

elements = list(range(1, n + 1))
prev_elements = []

def backtrack(idx):
    # base condition
    if len(prev_elements) == m:
        print(' '.join(map(str, prev_elements)))
        return

    for i in range(idx, n):
        prev_elements.append(elements[i])
        backtrack(i)
        prev_elements.pop()

backtrack(0)
