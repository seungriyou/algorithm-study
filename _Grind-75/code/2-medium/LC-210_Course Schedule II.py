# https://leetcode.com/problems/course-schedule-ii/

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """DFS"""
        # create graph & indegree array
        graph = [[] for _ in range(numCourses)]
        visited = [False] * numCourses
        for e, s in prerequisites:
            graph[s].append(e)

        res = []

        def dfs(pos):
            # base condition
            # (1) cycle 발생 시 False 반환
            if visited[pos] == -1:
                return False
            # (2) 이전에 방문했던 곳이라면 더이상 방문 X, True 반환
            if visited[pos] == 1:
                return True

            # recur
            visited[pos] = -1  # 현재 pos를 보고있다고 표시
            for npos in graph[pos]:
                # 다음 위치인 npos에서 cycle이 발생한다면 False 반환
                if not dfs(npos):
                    return False
            visited[pos] = 1  # 현재 pos를 방문했다고 표시

            # record
            res.append(pos)

            return True

        for i in range(numCourses):
            # i에서부터 시작해서 cycle이 발생한다면 전체 course를 들을 수 없으므로 [] 반환
            if not dfs(i):
                return []

        return res[::-1]

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """DFS"""
        # create graph & indegree array
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for e, s in prerequisites:
            graph[s].append(e)
            indegree[e] += 1

        res = []

        def dfs(pos):
            res.append(pos)
            indegree[pos] = -1  # mark as visited

            for npos in graph[pos]:
                indegree[npos] -= 1
                if indegree[npos] == 0:
                    dfs(npos)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return res if len(res) == numCourses else []

    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """topo sort"""
        from collections import deque

        # create graph & indegree array
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for e, s in prerequisites:
            graph[s].append(e)
            indegree[e] += 1

        q = deque(i for i, ind in enumerate(indegree) if ind == 0)
        res = []

        # topological sort
        while q:
            pos = q.popleft()
            res.append(pos)

            for npos in graph[pos]:
                indegree[npos] -= 1
                if indegree[npos] == 0:
                    q.append(npos)

        # if impossible to finish all courses, return empty array
        return res if len(res) == numCourses else []
