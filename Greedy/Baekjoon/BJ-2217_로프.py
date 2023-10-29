# https://www.acmicpc.net/problem/2217
import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()

max_weight = 0
"""
rope의 weight              | 10 15 21 30
함께 나눌 수 있는 rope 개수   | 4  3  2  1
"""
for i, r in enumerate(ropes):
    max_weight = max(max_weight, r * (N - i))
print(max_weight)
