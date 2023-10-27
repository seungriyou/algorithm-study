# https://www.acmicpc.net/problem/7569

import sys
from collections import deque
input = sys.stdin.readline

m, n, l = map(int, input().split())
# m: 가로, n: 세로, l: 상자 개수
tomatoes = []
not_riped_num = 0
riped = []
for i in range(l):
    box = []
    for j in range(n):
        row = list(map(int, input().split()))
        for k in range(m):
            if row[k] == 0:
                not_riped_num += 1
            elif row[k] == 1:
                riped.append(((i, j, k), 0))
        box.append(row)
    tomatoes.append(box)

dr = [0, 0, 0, 0, -1, 1]
dc = [0, 0, -1, 1, 0, 0]
dh = [-1, 1, 0, 0, 0, 0]

def bfs(start):
    """
    bfs가 끝나고,
        cnt == not_riped_num: 모두 익을 수 있는 것이므로 days를 반환
        cnt != not_riped_num: 모두 익을 수 없으므로 -1 반환
    """
    # 익은 토마토밖에 없다면, 0 반환
    # if len(riped) == m * n * l:
    #     return 0

    cnt = 0     # 안 익은 토마토 중에서 익게 된 토마토의 개수
    days = 0    # 최대 일 수 트래킹
    q = deque(start)

    while q:
        (h, r, c), d = q.popleft()

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nh = h + dh[i]

            if 0 <= nr < n and 0 <= nc < m and 0 <= nh < l and tomatoes[nh][nr][nc] == 0:
                tomatoes[nh][nr][nc] = 1
                days = d + 1
                cnt += 1
                q.append(((nh, nr, nc), days))

    return days if cnt == not_riped_num else -1

result = bfs(riped)
print(result)
