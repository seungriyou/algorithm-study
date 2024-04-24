# https://leetcode.com/problems/course-schedule/

from typing import List


class Solution:
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        DFS
            모든 경로를 살펴보기 위해
        """

        graph = [[] for _ in range(numCourses)]
        visited = set()
        current_path = set()

        for a, b in prerequisites:
            # b -> a
            graph[b].append(a)

        def is_cyclic(pos):
            # pos가 현재 보고 있는 경로에 포함된다면 cyclic
            if pos in current_path:
                return True

            # pos를 이전에 이미 방문했다면 방문 X
            if pos in visited:
                return False

            current_path.add(pos)  # 현재 pos를 보고있다고 표시
            for npos in graph[pos]:
                if is_cyclic(npos):
                    return True
            current_path.remove(pos)  # 현재 pos를 보고있다고 표시한 것 취소

            visited.add(pos)  # 현재 pos를 방문했다고 표시

            return False

        # 각 노드에서 출발
        for i in range(numCourses):
            if is_cyclic(i):
                return False

        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        DFS (visited 3단계)
            visited[i] = {0: unvisited, -1: being visited this time, 1: already visited}
        """

        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for a, b in prerequisites:
            # b -> a
            graph[b].append(a)

        def is_cyclic(pos):
            # pos가 현재 보고 있는 경로에 포함된다면 cyclic
            if visited[pos] == -1:
                return True

            # pos를 이전에 이미 방문했다면 방문 X
            if visited[pos] == 1:
                return False

            visited[pos] = -1  # 현재 pos를 보고있다고 표시
            for npos in graph[pos]:
                if is_cyclic(npos):
                    return True

            visited[pos] = 1  # 현재 pos를 방문했다고 표시

            return False

        # 각 노드에서 출발
        for i in range(numCourses):
            if is_cyclic(i):
                return False

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """topological sort"""
        from collections import deque

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            # b -> a
            graph[b].append(a)
            indegree[a] += 1

        def topo_sort():
            cnt = 0
            # indegree[i] == 0인 i부터 시작
            q = deque(i for i, ind in enumerate(indegree) if ind == 0)

            while q:
                pos = q.popleft()
                cnt += 1

                for npos in graph[pos]:
                    # npos의 indegree 감소
                    indegree[npos] -= 1
                    # npos의 indegree가 0이 되면 q에 넣기
                    if indegree[npos] == 0:
                        q.append(npos)

            return cnt

        cnt = topo_sort()

        return cnt == numCourses


###### review ######
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """3-State DFS"""

        # graph 만들기
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        # visited 뿐만 아니라, 현재 보고 있는 path를 기록하기 위한 current_path도 생성
        current_path, visited = set(), set()

        def has_cycle(pos):
            # visited에 있으면 이미 방문했으므로 방문 X
            if pos in visited:
                return False

            # current_path에 있으면 cycle 발생
            if pos in current_path:
                return True

            # current_path에 현재 node 기록 후, npos 순회하며 재귀적으로 확인
            current_path.add(pos)
            for npos in graph[pos]:
                if has_cycle(npos):
                    return True
            current_path.remove(pos)

            # 현재 node visited 처리
            visited.add(pos)

            return False

        # 모든 node 순회하며 검사
        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """topo sort (BFS)"""

        from collections import deque

        # graph 만들기
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # topological sort(bfs)
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        cnt = 0

        while q:
            pos = q.popleft()
            cnt += 1

            for npos in graph[pos]:
                indegree[npos] -= 1

                if indegree[npos] == 0:
                    q.append(npos)

        return cnt == numCourses
