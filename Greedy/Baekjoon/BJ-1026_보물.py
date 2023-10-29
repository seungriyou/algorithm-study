# https://www.acmicpc.net/problem/1026
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
answer = 0
for i, j in zip(a, b):
    answer += i * j
print(answer)
