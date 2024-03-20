# https://school.programmers.co.kr/learn/courses/30/lessons/42861
def solution(n, costs):
    """
    MST 문제: Prim
    """
    import heapq

    visited = [False] * n
    graph = [[] for _ in range(n)]
    for a, b, c in costs:
        graph[a].append((c, a, b))
        graph[b].append((c, b, a))

    def prim(start):
        visited[start] = True
        candidate = graph[start]
        heapq.heapify(candidate)
        mst = []
        total_cost = 0

        while candidate:
            c, a, b = heapq.heappop(candidate)

            if not visited[b]:  # b가 동일한 candidate 원소에 대해서는 계속해서 heappop 하게 된다!
                visited[b] = True
                mst.append((a, b))
                total_cost += c

                for ngbr in graph[b]:
                    if not visited[ngbr[2]]:
                        heapq.heappush(candidate, ngbr)

        return total_cost

    return prim(0)


def solution2(n, costs):
    """
    MST 문제: Kruskal
    """

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])

        return parent[x]

    def union_parent(parent, a, b):
        parent_a, parent_b = find_parent(parent, a), find_parent(parent, b)
        if parent_a < parent_b:
            parent[parent_b] = parent_a
        else:
            parent[parent_a] = parent_b

    def kruskal(costs):
        parent = list(range(n + 1))
        cost = cnt = 0

        costs.sort(key=lambda x: x[2])

        for a, b, c in costs:
            if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b)
                cost += c
                cnt += 1

                if cnt == n - 1:
                    break

        return cost

    return kruskal(costs)
