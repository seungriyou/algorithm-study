# https://www.acmicpc.net/problem/5014
import sys
from collections import deque
input = sys.stdin.readline

# 건물: 1층 ~ F층
# 강호: S층
# 스타트링크: G층
# 이동 단위: +U, -D

F, S, G, U, D = map(int, input().split())
result = -1
visited = [False] * (F + 1)
move = {U, -D}

q = deque([(S, 0)])     # (현재 방문 층, 현재까지의 이동 횟수)
visited[S] = True

while q:
    pos, c = q.popleft()
    # 스타트링크에 도착
    if pos == G:
        result = c  # result 갱신
        break
    # 엘레베이터 타고 이동
    for m in move:
        npos = pos + m
        if 1 <= npos <= F and not visited[npos]:
            q.append((npos, c + 1))
            visited[npos] = True

print(result if result != -1 else "use the stairs")

# =================
# TIP: visited array에 이동 횟수를 tracking 한다면 q에 tuple을 넣을 필요가 없다!
F, S, G, U, D = map(int, input().split())

def bfs(F, S, G, U, D):
    count = [-1] * (F + 1)  # count[i] == -1이면 i층은 아직 방문 X
    move = (U, -D)
    q = deque([S])
    count[S] = 0

    while q:
        pos = q.popleft()
        # 스타트링크 도착
        if pos == G:
            return count[pos]
        # 엘리베이터 타고 이동
        for m in move:
            npos = pos + m
            if 1 <= npos <= F and count[npos] == -1:
                q.append(npos)
                count[npos] = count[pos] + 1

    return "use the stairs"

print(bfs(F, S, G, U, D))
