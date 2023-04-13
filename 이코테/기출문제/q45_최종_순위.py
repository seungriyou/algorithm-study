# https://www.acmicpc.net/problem/3665

from collections import deque

for tc in range(int(input())):
    # 노드의 개수 입력
    n = int(input())
    # 모든 노드의 indegree는 0으로 초기화
    indegree = [0] * (n + 1)
    # graph의 인접 행렬
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    # 순위 정보 입력
    order = list(map(int, input().split()))
    # (높은 등수) -> (모든 낮은 등수)를 가리키도록 설정 & indegree 설정
    for i in range(n):
        for j in range(i + 1, n):
            graph[order[i]][order[j]] = True
            indegree[order[j]] += 1

    # 올해 변경된 순위 정보 입력
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b]: # a -> b인 경우
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else: # b -> a인 경우
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬
    result = [] # 알고리즘 수행 결과 (정렬 결과) 담을 리스트
    q = deque() # 큐

    # 처음 시작 시에는 indegree == 0인 것 넣기
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    only_one = True # 위상 정렬 결과가 오직 하나인지 여부 (-> ?) // 큐에 2개 이상의 원소가 있으면 False
    cycle = False # 그래프 내 사이클이 발생하는지 여부 (-> IMPOSSIBLE) // 큐가 비어있는 단계가 있으면 True

    # 정확히 노드의 개수만큼 반복 (while q 로 하지 않음***)
    for _ in range(n):
        # 큐가 비어있다면 사이클 발생
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개
        if len(q) >= 2:
            only_one = False
            break

        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # now와 연결된 원소들의 indegree를 하나 빼고, indegree == 0 되는 원소들을 큐에 넣기
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    # 사이클이 발생하는 경우
    if cycle:
        print("IMPOSSIBLE")
    elif not only_one:
        print("?")
    else:
        print(" ".join(map(str, result)))
