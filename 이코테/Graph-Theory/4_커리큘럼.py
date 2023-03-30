import copy
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        # 주의: j가 선수 과목이다!! i와 j의 순서에 주의하자.
        graph[j].append(i)

def topology_sort():
    q = deque()
    acc_time = copy.deepcopy(time)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for next_node in graph[now]:
            acc_time[next_node] = max(acc_time[next_node], acc_time[now] + time[next_node])
            indegree[next_node] -= 1
            # 주의: indegree == 0 되는 노드는 다시 queue에 넣기5
            if indegree[next_node] == 0:
                q.append(next_node)
    for i in range(1, n + 1):
        print(acc_time[i])

topology_sort()
