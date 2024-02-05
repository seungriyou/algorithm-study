# https://www.acmicpc.net/problem/1197
import sys; input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, parent_a, parent_b):
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

def kruskal(edges):
    result = 0  # mst의 가중치
    parent = list(range(V + 1))  # 자기 자신으로 parent 초기화
    cnt = 0     # mst에 포함되는 edges 수

    # edge의 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for a, b, weight in edges:
        parent_a = find_parent(parent, a)
        parent_b = find_parent(parent, b)
        # cycle이 발생하지 않는지 확인 후, union
        if parent_a != parent_b:
            union_parent(parent, parent_a, parent_b)
            result += weight
            cnt += 1
            # mst에 포함된 edges 수가 V - 1과 같다면 빠르게 return
            if cnt == V - 1:
                break

    return result

print(kruskal(edges))
