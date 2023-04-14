"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
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
parent = [i for i in range(n + 1)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 두 노드 i, j가 연결된 경우, union 연산 수행
            union_parent(parent, i + 1, j + 1)

plan = list(map(int, input().split()))

# plan에 속하는 모든 노드의 루트가 동일한지 확인
# (동일해야 가능한 계획)
result = True
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")
