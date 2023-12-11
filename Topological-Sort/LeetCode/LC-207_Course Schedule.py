# [LTC] 207 - Course Schedule
# https://leetcode.com/problems/course-schedule/

from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [sol1] topological sort (bfs)
        # -- cycle이 있으면 모든 원소를 방문하기 전에 queue가 빈다!
        indegree = [0] * numCourses             # -- 노드별 진입 차수
        graph = [[] for _ in range(numCourses)] # -- 방향 그래프

        for b, a in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        def topological_sort():
            cnt = 0
            # -- 진입 차수가 0인 노드부터 queue에 넣기
            q = deque([i for i in range(numCourses) if indegree[i] == 0])

            # -- queue가 빌 때까지 반복
            while q:
                now = q.popleft()
                cnt += 1
                for i in graph[now]:
                    # -- 다음 노드의 진입 차수 --
                    indegree[i] -= 1
                    # -- 다음 노드의 진입 차수가 0이 되면 queue에 넣기
                    if indegree[i] == 0:
                        q.append(i)

            return cnt

        cnt = topological_sort()

        return cnt == numCourses

sol = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(sol.canFinish(numCourses, prerequisites))
