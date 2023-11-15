# https://www.acmicpc.net/problem/9012
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = input().rstrip()
    stack = []
    for s in string:
        if s == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(s)
    print("NO" if stack else "YES")
