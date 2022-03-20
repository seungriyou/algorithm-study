# [BOJ] 1918 - 후위 표기

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def in_to_post(inorder: str) -> str:
    postorder = ""
    stack = []
    priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    for i in inorder:
        # 피연산자일 때
        if i.isalpha():
            postorder += i
        # ( 일 때
        elif i == '(':
            stack.append(i)
        # ) 일 때
        elif i == ')':
            while stack[-1] != '(':
                postorder += stack.pop()
            stack.pop()
        # 연산자일 때
        else:
            # next의 우선순위 <= stack의 top의 우선순위일 때
            while stack and priority[i] <= priority[stack[-1]]:
                postorder += stack.pop()
            stack.append(i)

    # stack이 비어있지 않을 때
    while stack:
        postorder += stack.pop()

    return postorder


print(in_to_post(input().strip()))
