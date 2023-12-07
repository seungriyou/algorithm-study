# https://www.acmicpc.net/problem/2417
import sys
input = sys.stdin.readline

n = int(input())
left, right = 0, n

while left <= right:
    mid = left + (right - left) // 2
    if mid * mid < n:
        left = mid + 1
    else:
        right = mid - 1

print(left)
