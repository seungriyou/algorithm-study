# https://www.acmicpc.net/problem/15683
import sys; input = sys.stdin.readline

# TIP: set()의 inplace 연산(update(), difference_update())에 대해 알아야 한다.
# TIP: 동, 서, 남, 북 방향에 대해 while 문을 통해서 확장하는 코드에 익숙해지자.

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cctvs = []      # 모든 cctv에 대해 (종류, r, c) 모으기
empty = 0       # 빈 칸 카운트
for i in range(N):
    for j in range(M):
        if 1 <= (type_num := office[i][j]) <= 5:
            cctvs.append((type_num, i, j))
        elif office[i][j] == 0:
            empty += 1


n_cctvs = len(cctvs)    # 전체 cctv의 개수
max_area = 0        # cctv가 감시하는 칸의 개수
visited = set()     # 방문한 칸의 좌표 기록


# 동, 남, 서, 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 각 cctv의 감시하는 방법
monitor_ds = {
    1: [(0,), (1,), (2,), (3,)],
    2: [(0, 2), (1, 3)],
    3: [(0, 1), (1, 2), (2, 3), (3, 0)],
    4: [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
    5: [(0, 1, 2, 3)]
}


def get_new_monitored_locs(r, c, ds):
    """
    해당 cctv가 감시할 수 있는 "한 가지 방법"에 대해 이전과 비교해서 "새롭게" 감시 대상이 된 칸의 좌표들을 반환하는 함수
    """
    _visited = set()        # 현재 방법에서 새롭게 감시 대상이 된 칸의 좌표

    # cctv가 감시할 수 있는 한 가지 방법에 속한 모든 방향에 대해 수행
    for d in ds:
        nr, nc = r, c   # cctv 위치로 재설정

        while True:
            nr += dr[d]
            nc += dc[d]

            # 범위를 벗어났거나 벽이면 종료
            if nr < 0 or nr >= N or nc < 0 or nc >= M or office[nr][nc] == 6:
                break

            # cctv이거나 이미 방문한 곳이면 넘어가기
            if office[nr][nc] != 0 or (nr, nc) in visited:
                continue

            # 방문 표시
            _visited.add((nr, nc))

    return _visited


def backtrack(idx):
    global max_area

    # base condition
    if idx == n_cctvs:
        # cctv가 감시하는 칸의 최대 개수 업데이트
        max_area = max(max_area, len(visited))
        return

    # recur
    for i in range(idx, n_cctvs):
        t, r, c = cctvs[i]      # cctv 종류, r, c

        # 해당 cctv의 각 감시 방법에 대해 수행
        for ds in monitor_ds[t]:
            _visited = get_new_monitored_locs(r, c, ds)
            visited.update(_visited)
            backtrack(i + 1)
            visited.difference_update(_visited)


backtrack(0)

print(empty - max_area)
