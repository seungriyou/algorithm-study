# https://www.acmicpc.net/problem/3986
import sys
input = sys.stdin.readline

N = int(input())
vocabs = [list(input().rstrip()) for _ in range(N)]
cnt = 0

def check(vocab):
    """vocab이 좋은 단어인지 판단하는 함수"""
    stack = []
    for v in vocab:
        if stack and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
    return len(stack) == 0

for vocab in vocabs:
    if len(vocab) % 2 != 0:
        continue
    cnt += check(vocab)

print(cnt)
