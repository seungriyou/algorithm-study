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

g = int(input())
p = int(input())

parent = [i for i in range(g + 1)]

result = 0 # 도킹 가능한 비행기의 최대 개수
for _ in range(p):
    root_node = find_parent(parent, int(input()))
    if root_node == 0:
        break
    union_parent(parent, root_node, root_node - 1) # 바로 왼쪽의 집합과 합치기
    result += 1

print(result)
