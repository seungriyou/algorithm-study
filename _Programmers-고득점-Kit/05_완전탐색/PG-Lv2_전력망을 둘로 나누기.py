# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque


def solution(n, wires):
    graph = [set() for _ in range(n + 1)]
    for a, b in wires:
        graph[a].add(b)
        graph[b].add(a)

    def get_tower_numbers(wire):
        """
        하나의 연결을 끊었을 때, 두 전력망 각각의 송전탑 개수 구하기
        """
        visited = set()
        cnt_1 = 0

        # 입력 받은 연결 끊기
        s, e = wire
        graph[s].remove(e)
        graph[e].remove(s)

        # 첫 번째 전력망 내 송전탑 개수 구하기
        q = deque([1])  # 랜덤하게 1번 노드 선택
        visited.add(1)

        while q:
            pos = q.popleft()
            cnt_1 += 1

            for npos in graph[pos]:
                if npos not in visited:
                    q.append(npos)
                    visited.add(npos)

        # 두 번째 전력망 내 송전탑 개수 구하기
        cnt_2 = n - cnt_1

        # 끊었던 연결 다시 복구
        graph[s].add(e)
        graph[e].add(s)

        return cnt_1, cnt_2

    min_diff = int(1e9)
    for wire in wires:
        cnt_1, cnt_2 = get_tower_numbers(wire)
        min_diff = min(min_diff, abs(cnt_1 - cnt_2))

    return min_diff


n, wires = 9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))   # should print 3
