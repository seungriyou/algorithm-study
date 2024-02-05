# https://www.acmicpc.net/problem/1717
import sys; input = sys.stdin.readline
# sys.setrecursionlimit(1_000_000)
#
# def find_parent(parent, x):
#     if x != parent[x]:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

def find_parent(parent, x):
    node = x
    while parent[node] != node:
        node = parent[node]
    parent[x] = node
    return node

def union_parent(parent, parent_a, parent_b):
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

n, m = map(int, input().split())
parent = list(range(n + 1))

for _ in range(m):
    op, a, b = map(int, input().split())
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if op == 0:
        # 집합 합치기
        union_parent(parent, parent_a, parent_b)

    else:
        # 같은 집합에 포함되어있는지 확인
        print("YES" if parent_a == parent_b else "NO")
