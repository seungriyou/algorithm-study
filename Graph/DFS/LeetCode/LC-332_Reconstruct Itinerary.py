# [LTC] 332 - Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # === DFS ===
        graph = defaultdict(list)
        for s, e in sorted(tickets, reverse=True):  # -- lexical order의 반대로 정렬
            graph[s].append(e)

        route = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())  # -- 반대로 정렬했으므로 뒤쪽부터 pop 가능
            route.append(start)

        dfs('JFK')
        return route[::-1]


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
sol = Solution()
print(sol.findItinerary(tickets))
