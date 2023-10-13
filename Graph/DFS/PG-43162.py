# [PG] 43162 - 네트워크 (Lv3)
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution_bfs(n, computers):
    from collections import deque

    #     graph = [[] for _ in range(n)]
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if computers[i][j]:
    #                 graph[i].append(j)
    #                 graph[j].append(i)

    visited = [False] * n
    cnt = 0

    def bfs(u):
        q = deque([u])

        while q:
            v = q.popleft()
            visited[v] = True

            # for w in graph[v]:
            #     if not visited[w]:
            #         q.append(w)

            for w in range(n):
                if not visited[w] and computers[v][w]:
                    q.append(w)

    for u in range(n):
        if not visited[u]:
            bfs(u)
            cnt += 1

    return cnt


def solution_dfs(n, computers):
    #     graph = [[] for _ in range(n)]
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if computers[i][j]:
    #                 graph[i].append(j)
    #                 graph[j].append(i)

    visited = [False] * n
    cnt = 0

    def dfs(u):
        visited[u] = True
        # for v in graph[u]:
        #     if not visited[v]:
        #         dfs(v)
        for v in range(n):
            if not visited[v] and computers[u][v]:
                dfs(v)

    for u in range(n):
        if not visited[u]:
            dfs(u)
            cnt += 1

    return cnt

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
assert 2 == solution_bfs(n, computers) == solution_dfs(n, computers)
