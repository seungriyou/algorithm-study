"""
- 사람: m명
    - 1번 사람은 1분에, ... m번 사람은 m분에 베이스캠프에서 출발하여 편의점으로 이동 시작
    - 출발 시간 전까지 격자 밖에 나와있음
    - 목표로 하는 편의점은 모두 다름
- 격자: n*n

[ 1분간 진행되는 행동 ]
1. 격자에 있는 사람들 모두, 본인이 가고 싶은 편의점 방향을 향해 1칸 이동
    - 최단거리로 이동
    - 최단거리로 움직이는 방법이 여러가지라면 ↑, ←, →, ↓ 의 우선 순위로 움직임
    - 최단거리: 상하좌우 인접 칸 중 이동 가능한 칸으로만 이동하여 도달하기까지 거쳐야 하는 칸의 수가 최소가 되는 거리

2. 편의점에 도착하면 멈추기
    - 이때부터 다른 사람들은 해당 칸을 지나갈 수 없음

3. 현재 시간이 t분이고 t <= m이라면, t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스캠프로 이동
    - 최단거리에 해당하는 베이스캠프로
    - 최단거리가 같은 베이스캠프가 여러 가지라면, 그 중 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스캠프로
    - 이때부터 다른 사람들은 해당 칸을 지나갈 수 없음

- grid: n*n
    - boolean
    - True: 지나갈 수 있는 곳 / False: 지나갈 수 없는 곳 (도착한 편의점 or 지나간 베이스캠프)
- 베이스캠프 위치: camps = set[tuple[int, int]]
- 사람 (idx=0 ~ m-1)
    - 값
        - loc: 현재 위치
        - store_loc: 가고 싶은 편의점 위치
        - arrived: 편의점에 도착했는지 여부
    - 행동
        - move_to_store: 가고 싶은 편의점을 향해 최단거리로 이동할 때의 다음 칸의 좌표로 이동하기
            1) arrived = True 라면 더이상 움직이지 X
            2) 최단거리로 이동하는 경로 구하기
                - 방법이 여러가지라면, ↑, ←, →, ↓ 의 우선 순위
                - grid가 True 인 칸으로만 이동 가능
        - arrive_at_store: not arrived && loc == store_loc 라면, 해당 편의점을 더이상 지날 수 없다고 표기 & 편의점 도착 여부 업데이트하기
            1) arrived = True
            2) grid = False
        - move_to_camp: 가고 싶은 편의점과 가장 가까이 있는 베이스캠프 좌표로 이동하기 & 더이상 지날 수 없다고 표기
            1) 편의점 ~ 베이스캠프 최단거리 / 행이 작은 / 열이 작은 베이스캠프 좌표로 이동
                - 편의점에서 출발 -> camps 내 좌표 중에 해당하는 게 있다면 선택
                - camps에서 remove
            2) grid = False

"""
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
camps = set()
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            camps.add((i, j))
        grid[i][j] = False
stores = [tuple(map(lambda x: x - 1, map(int, input().split()))) for _ in range(m)]


dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]

def valid(r, c):
    return 0 <= r < n and 0 <= c < n

class Person:
    def __init__(self, idx, store_loc):
        self.loc = None # 격자 밖
        self.idx = idx
        self.store_loc = store_loc
        self.arrived = False

    def __repr__(self):
        return f"<Person #{self.idx} loc={self.loc} store_loc={self.store_loc} arrived={'O' if self.arrived else 'X'}>"

    def move_to_store(self):
        """
        가고 싶은 편의점을 향해 최단거리로 이동할 때의 다음 칸의 좌표로 이동하기
        1) arrived = True 라면 더이상 움직이지 X
        2) 최단거리로 이동하는 경로 구하기
            - 방법이 여러가지라면, ↑, ←, →, ↓ 의 우선 순위
            - grid가 True 인 칸으로만 이동 가능
        """
        if not self.arrived and self.loc:
            # store_loc -> loc 까지의 최단 거리 구하기
            visited = [row[:] for row in grid]
            distances = [[0] * n for _ in range(n)]

            q = deque([self.store_loc])
            visited[self.store_loc[0]][self.store_loc[1]] = True
            visited[self.loc[0]][self.loc[1]] = False

            while q:
                r, c = q.popleft()

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if valid(nr, nc) and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
                        distances[nr][nc] = distances[r][c] + 1

            # loc의 ↑, ←, →, ↓ 중에서 가장 작은 칸으로 이동 (우선순위 주의)
            r, c = self.loc
            min_dist = n * n
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                # [주의] (1) (nr, nc)이 격자 내에 있고, (2) (nr, nc)이 갈 수 있는 곳이며 (3) 최소 거리일 때
                if valid(nr, nc) and not grid[nr][nc] and distances[nr][nc] < min_dist:
                    min_dist = distances[nr][nc]
                    self.loc = (nr, nc)

    def move_to_store2(self):
        """
        가고 싶은 편의점을 향해 최단거리로 이동할 때의 다음 칸의 좌표로 이동하기
        1) arrived = True 라면 더이상 움직이지 X
        2) 최단거리로 이동하는 경로 구하기
            - 방법이 여러가지라면, ↑, ←, →, ↓ 의 우선 순위
            - grid가 True 인 칸으로만 이동 가능
        """
        if not self.arrived and self.loc:
            # store_loc -> loc 까지의 최단 거리 구하기
            # visited 만들기 -> not visited 로만 이동하기
            visited = [row[:] for row in grid]

            q = deque([self.store_loc])
            visited[self.store_loc[0]][self.store_loc[1]] = True
            visited[self.loc[0]][self.loc[1]] = False

            while q:
                r, c = q.popleft()

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if valid(nr, nc) and not visited[nr][nc]:
                        if (nr, nc) == self.loc:
                            self.loc = (r, c)
                            break
                        q.append((nr, nc))
                        visited[nr][nc] = True

    def arrive_at_store(self):
        """
        not arrived && loc == store_loc 라면, 해당 편의점을 더이상 지날 수 없다고 표기 & 편의점 도착 여부 업데이트하기
            1) arrived = True
            2) grid = False
        """
        if not self.arrived and self.loc == self.store_loc:
            self.arrived = True
            grid[self.loc[0]][self.loc[1]] = True

    def move_to_camp(self):
        """
        가고 싶은 편의점과 가장 가까이 있는 베이스캠프 좌표로 이동하기 & 더이상 지날 수 없다고 표기
            1) 편의점 ~ 베이스캠프 최단거리 / 행이 작은 / 열이 작은 베이스캠프 좌표로 이동
                - 편의점에서 출발 -> camps 내 좌표 중에 해당하는 게 있다면 선택
                - camps에서 remove
            2) grid = False
        """

        visited = [row[:] for row in grid]

        q = deque([(0, *self.store_loc)])
        visited[self.store_loc[0]][self.store_loc[1]] = True

        min_dist = None
        min_camps = []  # (r, c)

        while q:
            d, r, c = q.popleft()

            # 최단거리의 베이스캠프를 모두 발견했으면 중단
            if min_dist and min_dist < d:
                break

            if (r, c) in camps:
                if not min_dist:
                    min_dist = d
                min_camps.append((r, c))

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if valid(nr, nc) and not visited[nr][nc]:
                    q.append((d + 1, nr, nc))
                    visited[nr][nc] = True

        camp = sorted(min_camps)[0]
        self.loc = camp
        grid[camp[0]][camp[1]] = True


people = [Person(idx, store_loc) for idx, store_loc in enumerate(stores)]

def is_everyone_arrived():
    for person in people:
        if not person.arrived:
            return False

    return True

if __name__ == "__main__":
    """
    1. 격자에 있는 사람들 모두, 본인이 가고 싶은 편의점 방향을 향해 1칸 이동
        - 최단거리로 이동
        - 최단거리로 움직이는 방법이 여러가지라면 ↑, ←, →, ↓ 의 우선 순위로 움직임
        - 최단거리: 상하좌우 인접 칸 중 이동 가능한 칸으로만 이동하여 도달하기까지 거쳐야 하는 칸의 수가 최소가 되는 거리
    
    2. 편의점에 도착하면 멈추기
        - 이때부터 다른 사람들은 해당 칸을 지나갈 수 없음
    
    3. 현재 시간이 t분이고 t <= m이라면, t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스캠프로 이동
        - 최단거리에 해당하는 베이스캠프로
        - 최단거리가 같은 베이스캠프가 여러 가지라면, 그 중 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스캠프로
        - 이때부터 다른 사람들은 해당 칸을 지나갈 수 없음
    """

    t = 0

    while True:
        # 1. 격자에 있는 사람들 모두, 본인이 가고 싶은 편의점 방향을 향해 1칸 이동
        for person in people:
            person.move_to_store()

        # 2. 편의점에 도착하면 멈추기
        for person in people:
            person.arrive_at_store()

        # 3. 현재 시간이 t분이고 t <= m이라면, t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스캠프로 이동
        if t < m:
            people[t].move_to_camp()

        t += 1

        if is_everyone_arrived():
            break

    print(t)
