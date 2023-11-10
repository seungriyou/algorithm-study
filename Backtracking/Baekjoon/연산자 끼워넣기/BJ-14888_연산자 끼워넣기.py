# https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline

# ===== w/o for loop =====
N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_result = -int(1e9)
min_result = int(1e9)

def backtrack(idx, prev, add, sub, mul, div):
    global max_result, min_result

    # base condition
    if idx == N:
        if prev > max_result:
            max_result = prev
        if prev < min_result:
            min_result = prev
        return

    # recur
    if add > 0:
        backtrack(idx + 1, prev + nums[idx], add - 1, sub, mul, div)
    if sub > 0:
        backtrack(idx + 1, prev - nums[idx], add, sub - 1, mul, div)
    if mul > 0:
        backtrack(idx + 1, prev * nums[idx], add, sub, mul - 1, div)
    if div > 0:
        backtrack(idx + 1, int(prev / nums[idx]), add, sub, mul, div - 1)

backtrack(1, nums[0], ops[0], ops[1], ops[2], ops[3])

print(max_result)
print(min_result)


# ===== w/ for loop ====
N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_result = -int(1e9)
min_result = int(1e9)

def backtrack(idx, prev):
    global max_result, min_result

    # base condition
    if idx == N:
        if prev > max_result:
            max_result = prev
        if prev < min_result:
            min_result = prev
        return

    # recur
    for i in range(4):
        if not ops[i]:
            continue

        ops[i] -= 1
        if i == 0:
            backtrack(idx + 1, prev + nums[idx])
        elif i == 1:
            backtrack(idx + 1, prev - nums[idx])
        elif i == 2:
            backtrack(idx + 1, prev * nums[idx])
        else:
            backtrack(idx + 1, int(prev / nums[idx]))
        ops[i] += 1

backtrack(1, nums[0])

print(max_result)
print(min_result)
