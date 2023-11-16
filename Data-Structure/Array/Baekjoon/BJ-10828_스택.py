# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command = input().split()
    op = command[0]
    if op == "push":
        stack += [command[1]]
    elif op == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif op == "size":
        print(len(stack))
    elif op == "empty":
        print(0 if stack else 1)
    elif op == "pop":
        if stack:
            print(stack[-1])
            stack = stack[:-1]
        else:
            print(-1)
