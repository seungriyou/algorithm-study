# https://www.acmicpc.net/problem/1647
import sys; input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, parent_a, parent_b):
    # 어차피 find를 할 것이므로 union 최적화 가능
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

def kruskal(edges):
    result = 0  # 유지비의 합의 최솟값
    parent = list(range(N + 1))
    max_c = 0   # mst를 구성하는 edge들의 유지비 중 최대 유지비 (두 개의 마을로 나눌 때 해당 edge를 삭제)
    cnt = 0     # N - 1 개의 edges를 모두 mst에 포함했으면 빠르게 return 하기 위한 목적

    # 유지비 기준 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for a, b, c in edges:
        parent_a = find_parent(parent, a)
        parent_b = find_parent(parent, b)
        # a와 b를 연결함으로써 cycle이 발생하지 않는다면 union
        if parent_a != parent_b:
            union_parent(parent, parent_a, parent_b)
            result += c
            max_c = c
            cnt += 1
            # mst에 N - 1개의 edges가 포함되었으면 빠르게 종료
            if cnt == N - 1:
                break

    return result - max_c

print(kruskal(edges))
