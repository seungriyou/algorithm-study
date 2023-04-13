"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""

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


n, m = map(int, input().split())
parent = [i for i in range(n)]

edges = []
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()

total_cost = 0
spent_cost = 0

for edge in edges:
    cost, x, y = edge
    total_cost += cost
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        spent_cost += cost

print(total_cost - spent_cost)
