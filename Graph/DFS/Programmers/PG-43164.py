# [PG] 43164 - 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    from collections import defaultdict

    n = len(tickets) + 1

    graph = defaultdict(list)
    for s, d in sorted(tickets):
        graph[s].append(d)

    def dfs(start, route):
        if len(route) == n:
            return route

        for i in range(len(graph[start])):
            # TODO: 더 최적화 할 수 없을까? pop(i), insert(i, ngbr) 말고, reverse sort해서 그냥 pop(), append(ngbr) 할 수 있는 방법이 없을까?
            ngbr = graph[start].pop(i)
            result = dfs(ngbr, route + [ngbr])
            graph[start].insert(i, ngbr)

            if result:
                return result

    return dfs('ICN', ['ICN'])


def solution2(tickets):
    from collections import defaultdict

    graph = defaultdict(list)
    for s, d in sorted(tickets, reverse=True):
        graph[s].append(d)

    route = []

    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop())
        route.append(start)

    dfs('ICN')

    return route[::-1]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
assert ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] == solution(tickets) == solution2(tickets)
