# https://www.acmicpc.net/problem/15664
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
    prev = 0    # 같은 level에서 직전에 본 숫자 기록
    for i in range(idx, N):
        if prev != nums[i]:
            prev_elements.append(nums[i])
            prev = nums[i]
            backtrack(i + 1)
            prev_elements.pop()

backtrack(0)
