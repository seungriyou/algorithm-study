# https://www.acmicpc.net/problem/15656
import sys
input = sys.stdin.readline

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
    for e in nums:
        prev_elements.append(e)
        backtrack()
        prev_elements.pop()

backtrack()
