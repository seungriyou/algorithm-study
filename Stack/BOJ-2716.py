# [BOJ] 2716 - 원숭이 매달기

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def monkey(tree: str) -> int:
    depth = 0
    stack = []
    for t in tree:
        if t == '[':
            stack.append(t)
            depth = max(depth, len(stack))
        else:
            stack.pop()
    return 2 ** depth


for _ in range(int(input())):
    tree = input().strip()
    print(monkey(tree))
