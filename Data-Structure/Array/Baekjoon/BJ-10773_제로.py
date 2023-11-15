# https://www.acmicpc.net/problem/10773
import sys
input = sys.stdin.readline

K = int(input())

stack = [0]
for _ in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
