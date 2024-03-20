"""
n*n 격자
m = 팀 개수
k = 라운드 수

0 = 빈칸 / 1 = 머리사람 / 2 = 나머지 / 3 = 꼬리사람 / 4 = 이동 선

[ 각 라운드 ]
1. 머리사람을 따라 한 칸씩 이동
2. 공 던지기 [(0, 1), (-1, 0), (0, -1), (1, 0)] / 1 ~ 4n 라운드
3. 공이 던져지는 선에 사람이 있다면, 최초에 만나게 되는 사람이 공을 얻어 점수 얻음
    - 해당 사람이 머리사람을 시작으로 k 번째 사람이라면 k^2 만큼 점수 얻음
    - 공을 획득한 팀의 경우, 머리사람 <-> 꼬리사람

[ 필요한 동작 ]
- 팀에 속하는 사람들의 좌표는 [(머리사람), ..., (꼬리사람)] 순서로!
- 한 칸 이동
- 공 던지기
    - 맞은 사람의 팀, 순서 구하기 -> 점수
    - 해당 팀의 좌표 reverse
"""

from collections import deque

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

scores = [0] * m


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]


def find_team_members(r, c, visited):
    visited[r][c] = True
    team = deque([(r, c)])
    q = deque([])
    # [주의] 1 인접 칸이 2, 4가 아닌 2, 3일 수도 있으므로, 2 칸 부터 시작하도록
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if is_valid(nr, nc) and not visited[nr][nc] and grid[nr][nc] == 2:
            team.append((nr, nc))
            visited[nr][nc] = True
            q.append((nr, nc))
            break

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # (1) 범위를 벗어나지 않고, (2) 방문하지 않았으며, (3) 값이 2 또는 3인 경우에만
            if is_valid(nr, nc) and not visited[nr][nc] and grid[nr][nc] in (2, 3):
                team.append((nr, nc))
                visited[nr][nc] = True
                q.append((nr, nc))

                if grid[nr][nc] == 3:
                    return team


def move_one_cell(team):
    # <1> 기존 head와 tail을 각각 2와 4로 변경
    hr, hc = team[0]
    tr, tc = team.pop()
    grid[hr][hc] = 2
    grid[tr][tc] = 4

    # <2> 새로운 head 찾고 1로 변경
    for i in range(4):
        nr, nc = hr + dr[i], hc + dc[i]
        if is_valid(nr, nc) and grid[nr][nc] == 4:
            team.appendleft((nr, nc))
            grid[nr][nc] = 1
            break

    # <3> 새로운 tail 3으로 변경
    r, c = team[-1]
    grid[r][c] = 3


def move():
    for team in teams:
        move_one_cell(team)


def find_people_loc(r, c, dr, dc):
    while is_valid(r, c):
        if grid[r][c] not in (0, 4):
            return (r, c)
        else:
            r, c = r + dr, c + dc
    return None


def find_team_and_order(loc):
    for i, team in enumerate(teams):
        for j, _loc in enumerate(team):
            if _loc == loc:
                return i, j + 1  # (team id, order)


def reverse_team(team):
    # 1. grid 값 변경
    hr, hc = team[0]
    tr, tc = team[-1]
    grid[hr][hc], grid[tr][tc] = grid[tr][tc], grid[hr][hc]
    # 2. 좌표 순서 뒤집기
    team.reverse()


def throw_ball(round_n):
    # 1. 시작 위치 r, c & 변위 dr, dc 구하기
    dd = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    d, m = divmod(round_n, n)
    dr, dc = dd[(d % 4)]
    if (nd := d % 4) == 0:
        r, c = m, 0
    elif nd == 1:
        r, c = n - 1, m
    elif nd == 2:
        r, c = n - m - 1, n - 1
    elif nd == 3:
        r, c = 0, n - m - 1

    # 2. 이동하면서 4가 아닌 값이 나오는 경우, stop
    if hit_loc := find_people_loc(r, c, dr, dc):
        # 3. 해당 좌표가 어느 팀에 속하는지, 몇 번째 원소인지 알기
        i, k = find_team_and_order(hit_loc)

        # 4. 해당 팀의 점수
        scores[i] += k * k

        # 5. 해당 팀은 뒤집기
        reverse_team(teams[i])


if __name__ == "__main__":
    # <1> 팀 정보 구하기
    teams = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 머리사람을 발견한 경우
            if grid[i][j] == 1:
                team = find_team_members(i, j, visited)
                teams.append(team)

    # <2> 라운드 돌기
    for round_n in range(k):
        # 1. 머리사람 따라 이동
        move()

        # 2. 공 던지기
        throw_ball(round_n)

    # <3> 점수 총합 구하기
    print(sum(scores))
