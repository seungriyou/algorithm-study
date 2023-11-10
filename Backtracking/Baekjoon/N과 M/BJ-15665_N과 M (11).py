# https://www.acmicpc.net/problem/15665
import sys
input = sys.stdin.readline

# ===== manage duplicates w/ prev =====
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

prev_elements = []

def backtrack():
    # base condition
    if len(prev_elements) == M:
        print(*prev_elements)
        return

    # recur
    prev = 0
    for i in range(N):
        if prev != nums[i]:
            prev = nums[i]
            prev_elements.append(nums[i])

            backtrack()

            prev_elements.pop()

backtrack()


# ===== manage duplicates w/o prev =====
N, M = map(int, input().split())
nums = list(set(map(int, input().split()))) # -- 중복 제거
nums.sort()

prev_elements = []

def backtrack():
    # base condition
    if len(prev_elements) == M:
        print(*prev_elements)
        return

    # recur
    for i in range(len(nums)):
        prev_elements.append(nums[i])
        backtrack()
        prev_elements.pop()

backtrack()
