# https://www.acmicpc.net/problem/2887

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n + 1)]

# 총 간선의 개수 = 3 * (N - 1)
edges = [] # 전체 간선을 담을 리스트
result = 0 # 최종 비용

x = []
y = []
z = []

# sorting 후에도 같은 행성끼리는 x, y, z에 표시를 해주어야 하므로
for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

for i in range(n - 1):
    # (cost, a, b) -> cost 기준으로 sorting을 위함
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# min(|xa-xb|, |ya-yb}, |za-zb|) 의 효과
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
