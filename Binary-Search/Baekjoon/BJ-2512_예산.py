# https://www.acmicpc.net/problem/2512
import sys; input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

left = 1
right = max(budgets)
result = 0

def get_sum(ub):
    return sum(min(ub, budget) for budget in budgets)

while left <= right:
    mid = (left + right) // 2

    if get_sum(mid) > M:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)
