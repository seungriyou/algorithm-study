# [LTC] 207 - Course Schedule
# https://leetcode.com/problems/course-schedule/

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # === DFS (final) ===
        graph = [[] for _ in range(numCourses)]  # -- 방향 그래프
        for b, a in prerequisites:
            graph[a].append(b)

        visited = set()
        current_path = set()

        def dfs(i):
            # cycle 이면 False
            if i in visited:
                return False
            # 이미 현재 path에서 방문했던 node 라면 True (가지치기)
            if i in current_path:
                return True

            visited.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited.remove(i)

            current_path.add(i)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

    def canFinish_dfs_prev(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [sol2] dfs (cycle detection)
        # https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
        # visited => 0, 1, 2로 구분해서 할당하면 current_path를 사용하지 않아도 ok
        # graph coloring 문제 찾아보기
        graph = [[] for _ in range(numCourses)]  # -- 방향 그래프
        for b, a in prerequisites:
            graph[a].append(b)

        visited = [False] * numCourses
        current_path = [False] * numCourses

        def is_cyclic(node):
            visited[node] = True
            current_path[node] = True  # -- whether the node is a part of the current path

            for next_node in graph[node]:
                if not visited[next_node]:
                    if is_cyclic(next_node):
                        return True
                elif current_path[next_node]:
                    return True

            current_path[node] = False
            return False

        for i in range(numCourses):
            if not visited[i]:
                if is_cyclic(i):
                    return False
        return True

sol = Solution()
# numCourses = 20
# prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.canFinish(numCourses, prerequisites))
