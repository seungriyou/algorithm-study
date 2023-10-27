import sys
input = sys.stdin.readline

"""
subset 문제
-> base condition 설정할 필요 없이, 매 단계마다 확인/기록하면 된다.
"""

N, S = map(int, input().split())
nums = list(map(int, input().split()))

# ===============
# basic
# ===============

# result = []
prev_elements = []
cnt = 0

def backtrack(idx):
    global cnt

    if prev_elements and sum(prev_elements) == S:
        # result.append(prev_elements[:])
        cnt += 1

    # recur
    for i in range(idx, N):
        prev_elements.append(nums[i])
        backtrack(i + 1)
        prev_elements.pop()

backtrack(0)
# print(len(result))
print(cnt)

# ===============
# slowest :(
# ===============

# result = []
cnt = 0

def backtrack(idx, path):
    global cnt

    if path and sum(path) == S:
        # result.append(path)
        cnt += 1

    # recur
    for i in range(idx, N):
        backtrack(i + 1, path + [nums[i]])

backtrack(0, [])
# print(len(result))
print(cnt)

# ===============
# fastest! :)
# ===============

cnt = 0

def backtrack(idx, acc_sum):
    global cnt

    if idx and acc_sum == S:
        cnt += 1

    # recur
    for i in range(idx, N):
        backtrack(i + 1, acc_sum + nums[i])

backtrack(0, 0)
print(cnt)

# ================
cnt = 0

def backtrack(idx, acc_sum):
    global cnt

    # recur
    for i in range(idx, N):
        tmp = acc_sum + nums[i]
        if tmp == S:
            cnt += 1
        backtrack(i + 1, tmp)

backtrack(0, 0)
print(cnt)
