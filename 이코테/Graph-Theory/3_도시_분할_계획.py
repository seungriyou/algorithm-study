n, m = map(int, input().split())
edges = []

parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

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

edges.sort()

max_cost = 0
total_cost = 0
for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        total_cost += c
        max_cost = c
        union_parent(parent, a, b)

print(total_cost - max_cost)
