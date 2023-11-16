# https://www.acmicpc.net/problem/10866
import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    command = input().split()
    op = command[0]
    if op == "push_front":
        q = [command[1]] + q
    elif op == "push_back":
        q.append(command[1])
    elif op == "pop_front":
        if q:
            print(q[0])
            q = q[1:]
        else:
            print(-1)
    elif op == "pop_back":
        if q:
            print(q[-1])
            q = q[:-1]
        else:
            print(-1)
    elif op == "size":
        print(len(q))
    elif op == "empty":
        print(int(not q))
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
