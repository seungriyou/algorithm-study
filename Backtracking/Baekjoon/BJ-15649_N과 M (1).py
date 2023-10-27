# [BJ] 15649 - N과 M (1)
# https://www.acmicpc.net/problem/15649

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

elements = list(range(1, n + 1))
prev_elements = []

def backtrack():
    # base condition
    if len(prev_elements) == m:
        print(' '.join(map(str, prev_elements)))
        return

    for e in elements:
        if e not in prev_elements:
            prev_elements.append(e)
            backtrack()
            prev_elements.pop()

backtrack()
