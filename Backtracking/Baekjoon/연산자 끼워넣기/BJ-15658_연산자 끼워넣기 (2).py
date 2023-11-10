# https://www.acmicpc.net/problem/15658
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = int(1e9)
max_value = -int(1e9)

def backtrack(idx, result, add, sub, mul, div):
    global min_value, max_value

    # base condition
    if idx == N:
        min_value = min(min_value, result)
        max_value = max(max_value, result)
        return

    # recur
    if add > 0:
        backtrack(idx + 1, result + nums[idx], add - 1, sub, mul, div)
    if sub > 0:
        backtrack(idx + 1, result - nums[idx], add, sub - 1, mul, div)
    if mul > 0:
        backtrack(idx + 1, result * nums[idx], add, sub, mul - 1, div)
    if div > 0:
        backtrack(idx + 1, int(result / nums[idx]), add, sub, mul, div - 1)

backtrack(1, nums[0], add, sub, mul, div)

print(max_value)
print(min_value)
