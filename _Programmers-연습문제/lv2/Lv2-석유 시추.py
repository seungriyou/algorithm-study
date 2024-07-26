# https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque


def solution(land):
    n, m = len(land), len(land[0])

    # amounts[i]: i - 1 번째 시추관을 통해 뽑을 수 있는 석유량
    amounts = [0] * m

    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < m

    def bfs(r, c):
        q = deque([(r, c)])
        # visited -> 1을 0으로 바꾸기
        land[r][c] = 0
        # 현재 석유 덩어리의 크기
        size = 1
        # 현재 석유 덩어리에 속하는 시추관 위치 모으기
        locs = {c}

        # BFS 수행
        while q:
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if is_valid(nr, nc) and land[nr][nc] == 1:
                    q.append((nr, nc))
                    land[nr][nc] = 0
                    size += 1
                    locs.add(nc)

        # amounts에 반영
        for loc in locs:
            amounts[loc] += size

    # lands를 순회하며 모든 석유량 구하기
    for i in range(n):
        for j in range(m):
            if land[i][j]:
                bfs(i, j)

    return max(amounts)
