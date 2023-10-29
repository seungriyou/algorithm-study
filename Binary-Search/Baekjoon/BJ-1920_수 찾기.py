# https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

# ===== set ======
# N = int(input())
# nums = set(map(int, input().split()))
# M = int(input())
# compare = list(map(int, input().split()))
#
# for c in compare:
#     print(1 if c in nums else 0)

# ===== binary search =====
N = int(input())
nums = list(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))

nums.sort()

def binary_search(num):
    left, right = 0, N - 1
    while left <= right:
        mid = left + (right - left) // 2
        if num < nums[mid]:
            right = mid - 1
        elif num > nums[mid]:
            left = mid + 1
        else:
            return 1
    return 0

for c in compare:
    print(binary_search(c))
