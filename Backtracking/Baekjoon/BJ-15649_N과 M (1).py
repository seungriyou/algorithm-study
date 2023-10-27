# [BJ] 15649 - N과 M (1)
# https://www.acmicpc.net/problem/15649

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(range(1, n + 1))
prev_elements = []

def backtrack(elements):
    # base condition
    if len(prev_elements) == m:
        print(" ".join(map(str, prev_elements)))
        return

    # recur
    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)

        prev_elements.append(e)
        backtrack(next_elements)
        prev_elements.pop()

backtrack(nums)
