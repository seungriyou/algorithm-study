# https://www.acmicpc.net/problem/5397
import sys
input = sys.stdin.readline

"""1406번 문제와 마찬가지로 stack을 이용하자!"""

N = int(input())
for _ in range(N):
    stack1 = [] # 커서의 왼쪽
    stack2 = [] # 커서의 오른쪽

    string = list(input().rstrip())
    for s in string:
        if s == "<":
            if stack1:
                stack2.append(stack1.pop())
        elif s == ">":
            if stack2:
                stack1.append(stack2.pop())
        elif s == "-":
            if stack1:
                stack1.pop()
        else:
            stack1.append(s)

    stack2.reverse()

    print("".join(stack1) + "".join(stack2))
