# [BJ] 15651 - N과 M (3)
# https://www.acmicpc.net/problem/15651

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

elements = list(range(1, n + 1))
prev_elements = []

def backtrack():
    # base condition
    if len(prev_elements) == m:
        print(*prev_elements)
        return

    # recur
    for i in range(n):
        prev_elements.append(elements[i])
        backtrack()
        prev_elements.pop()

backtrack()
