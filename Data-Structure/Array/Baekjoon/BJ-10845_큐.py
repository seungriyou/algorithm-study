# https://www.acmicpc.net/problem/10845
import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    command = input().split()
    op = command[0]
    if op == "push":
        q.append(command[1])
    elif op == "pop":
        if q:
            print(q[0])
            q = q[1:]
        else:
            print(-1)
    elif op == "size":
        print(len(q))
    elif op == "empty":
        print(0 if q else 1)
    elif op == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif op == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
