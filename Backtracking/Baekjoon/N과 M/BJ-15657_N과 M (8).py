# https://www.acmicpc.net/problem/15657
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

prev_elements = []

def backtrack(idx):
    # base condition
    if len(prev_elements) == M:
        print(*prev_elements)
        return

    # recur
    for i in range(idx, N):
        prev_elements.append(nums[i])
        backtrack(i)
        prev_elements.pop()

backtrack(0)
