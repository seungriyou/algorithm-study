# https://www.acmicpc.net/problem/15663
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
    prev = 0        # 같은 level에서 직전에 본 숫자 기록
    for i in range(N):
        if not seen[i] and prev != nums[i]:
            prev_elements.append(nums[i])
            prev = nums[i]
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
        return

    # recur
    prev = 0
    for i in range(len(elements)):
        if prev != elements[i]:
            next_elements = elements[:]
            next_elements.pop(i)

            prev_elements.append(elements[i])
            prev = elements[i]
            backtrack(next_elements)
            prev_elements.pop()


backtrack(nums)
