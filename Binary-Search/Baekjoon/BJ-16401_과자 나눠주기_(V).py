# https://www.acmicpc.net/problem/16401
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

# ===== sol 1 =====
left, right = 1, max(snacks)
max_len = 0

while left <= right:
    mid = left + (right - left) // 2
    cnt = 0
    for snack in snacks:
        cnt += snack // mid

    if cnt < M:
        right = mid - 1
    else:
        max_len = mid   # max_len = max(max_len, mid)
        left = mid + 1

print(max_len)

# ===== sol 2 (much faster) =====
left, right = 1, max(snacks)

while left <= right:
    mid = left + (right - left) // 2
    cnt = sum(snack // mid for snack in snacks)

    if cnt < M:
        right = mid - 1
    else:
        left = mid + 1

print(right)
