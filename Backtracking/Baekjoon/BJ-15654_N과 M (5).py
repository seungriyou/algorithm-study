# https://www.acmicpc.net/problem/15654

import sys
input = sys.stdin.readline

# ===== w/ seen =====
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

prev_elements = []
seen = [False] * N

def backtrack():
    # base condition
    if len(prev_elements) == M:
        print(*prev_elements)
        return

    # recur
    for i in range(N):
        if not seen[i]:
            prev_elements.append(nums[i])
            seen[i] = True

            backtrack()

            prev_elements.pop()
            seen[i] = False

backtrack()


# ===== w/o seen =====
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

prev_elements = []

def backtrack(elements):
    # base condition
    if len(prev_elements) == M:
        print(*prev_elements)

    # recur
    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)

        prev_elements.append(e)
        backtrack(next_elements)
        prev_elements.pop()

backtrack(nums)
