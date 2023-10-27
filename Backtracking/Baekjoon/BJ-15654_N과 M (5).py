# https://www.acmicpc.net/problem/15654

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

# result = []
prev_elements = []

def backtrack(elements):
    # base condition
    if len(prev_elements) == M:
        print(" ".join(map(str, prev_elements)))
        # result.append(prev_elements[:])

    # recur
    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)

        prev_elements.append(e)
        backtrack(next_elements)
        prev_elements.pop()

backtrack(nums)
# print(result)
