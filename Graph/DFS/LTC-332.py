# [LTC] 332 - Reconstruct Itinerary

from typing import List
from collections import defaultdict


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):  # 사전식 순서의 반대로 sort 하면 pop(0) 대신 pop() 사용 가능
        graph[a].append(b)

    route = []
    def dfs(a):
        while graph[a]:
            # dfs(graph[a].pop(0))    # 어휘순 방문해야 하므로 pop(0)으로 첫 번째 원소 pop
            dfs(graph[a].pop())
        route.append(a) # 역순으로 생성될 것
        # print(route)

    dfs('JFK')
    return route[::-1]


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(tickets))
