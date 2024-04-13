# https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner
"""
- 미로: N * N
    - 빈 칸: 참가자가 이동 가능한 칸
    - 벽: 참가자가 이동 불가능
        - 1 ~ 9 의 내구도
        - 회전할 때, 내구도가 1씩 깎임
        - 내구도가 0이 되면 빈 칸으로 변경됨
    - 출구: 참가자가 도달하면 즉시 탈출
- K 초
    - K 초 전에 모든 참가자가 탈출 성공 시 게임 끝

- 모든 참가자의 이동거리 합, 출구 좌표 출력

[ 1초마다 ]
1. 모든 참가자가 한 칸씩 이동
    - 두 위치의 최단 거리: |x1 - x2| + |y1 - y2|
    - 모든 참가자는 동시에 움직임
    - 상하좌우, 벽이 없는 곳으로 이동
    - 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단거리가 가까워야 함
    - 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것이 우선
    - 참가자가 움직일 수 없다면 움직이지 X
    - 한 칸에 2명 이상의 참가자가 있을 수 있음

2. 미로 회전
    - 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡는다.
    - 가장 작은 크기의 정사각형이 여러 개라면, 좌상단 r 좌표가 작은 것이 우선, 그래도 같으면 c 좌표가 작은 것이 우선
    - 선택된 정사각형은
        - 시계 방향으로 90도 회전
        - 회전된 벽은 내구도가 1씩 깎임 (0이 되면 빈 칸으로 변경)

[ Person ]
- 값
    - idx
    - loc: (r, c)
    - distance: 이동한 거리
    - arrived: 출구 도착 여부
- 동작
    - 다음 위치로 이동하는 동작
        - 상하좌우별로 최단거리 구하고, 가장 작은 것 구하기
        - 여러 개라면, 상하로 움직이는 것이 우선

        - 움직였다면 distance++
        - 출구에 도달했다면 arrived = True
    - square에 포함되면 위치 시계방향 90도 회전
        - input: start, end
        -

[ 필요한 동작 ]
- get_min_distance(): 최단 거리 구하기
- find_square(): 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 찾기
    - 여러 개라면, 좌상단 r 좌표가 작은 것, 같으면 c 좌표가 작은 것이 우선
- rotate_square(): 정사각형 회전
    - 시계 방향으로 90도 회전
    - 회전된 벽은 내구도가 1씩 깎임 (0이 되면 빈 칸으로 변경)
    - 사각형 내에 포함된 참가자의 loc도 옮겨주기
- is_everyone_arrived(): 모든 참가자가 탈출했는지 확인
"""

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
people = [tuple(map(lambda x: x - 1, map(int, input().split()))) for _ in range(M)]
exit = tuple(map(lambda x: x - 1, map(int, input().split())))

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

class Person:
    def __init__(self, idx, loc, distance=0, arrived=False):
        self.idx = idx
        self.loc = loc
        self.distance = distance
        self.arrived = arrived

    def __repr__(self):
        return f"<Person #{self.idx} loc={self.loc} distance={self.distance} arrived={self.arrived}>"

    def _can_go(self, r, c):
        return 0 <= r < N and 0 <= c < N and not grid[r][c]

    def move(self):
        """
        - 두 위치의 최단 거리: |x1 - x2| + |y1 - y2|
        - 모든 참가자는 동시에 움직임
        - 상하좌우, 벽이 없는 곳으로 이동
        - 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단거리가 가까워야 함
        - 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것이 우선
        - 참가자가 움직일 수 없다면 움직이지 X
        - 한 칸에 2명 이상의 참가자가 있을 수 있음
        """
        if not self.arrived:
            # 현재 위치에서 출구까지의 최단 거리 구하기
            curr_min = get_min_distance(self.loc, exit)
            new_loc = None

            # 상, 하, 좌, 우 순서로, 현재 위치에서의 최단 거리보다 작은 것들을
            r, c = self.loc
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if self._can_go(nr, nc) and curr_min > (new_min := get_min_distance((nr, nc), exit)):
                    curr_min = new_min
                    new_loc = (nr, nc)
                    break

            # 움직일 수 있다면 움직이기
            if new_loc:
                self.loc = new_loc
                self.distance += 1
                # 출구에 도달했다면
                if self.loc == exit:
                    self.arrived = True

    def rotate(self, start, end):
        if not self.arrived:
            sr, sc = start
            er, ec = end
            r, c = self.loc

            # square에 속하는 경우에만 rotate
            if sr <= r <= er and sc <= c <= ec:
                # square의 row 수
                row = er - sr + 1

                # square 내에서의 좌표
                nr, nc = r - sr, c - sc

                # square를 시계 방향으로 90도 돌렸을 때의 위치
                self.loc = (nc + sr, row - nr - 1 + sc)



people = [Person(i, loc) for i, loc in enumerate(people)]

def get_min_distance(src, dst):
    return abs(src[0] - dst[0]) + abs(src[1] - dst[1])

def _is_valid(sr, sc, _len, locs):
    # NOTE: 이중 포문 돌릴 필요 없이, 범위만 확인하면 된다!!
    is_exit = is_person = False

    # row 범위: sr ~ sr + _len - 1
    # col 범위: sc ~ sc + _len - 1
    er, ec = sr + _len - 1, sc + _len - 1

    # 출구 확인
    if sr <= exit[0] <= er and sc <= exit[1] <= ec:
        is_exit = True

    # 참가자 확인
    for loc in locs:
        if sr <= loc[0] <= er and sc <= loc[1] <= ec:
            is_person = True
            break

    return is_exit and is_person

def find_square():
    # NOTE: brute force!

    # 참가자들의 위치
    people_locs = set(person.loc for person in people if not person.arrived)

    # length를 2 ~ N까지 늘려가면서
    for _len in range(2, N + 1):
        # square의 왼쪽 상단부터
        for sr in range(N - _len + 1):
            for sc in range(N - _len + 1):
                if _is_valid(sr, sc, _len, people_locs):
                    return (sr, sc), (sr + _len - 1, sc + _len - 1)

def rotate_square(start, end, grid):
    global exit
    """
    start: square의 좌측상단 좌표
    end: square의 우측하단 좌표
    """
    sr, sc = start
    er, ec = end

    # square 뜯어내기
    square = [grid[r][sc: ec + 1] for r in range(sr, er + 1)]

    # square 시계방향으로 90도 돌리기
    square = list(zip(*square[::-1]))

    # grid 수정하기
    for r, square_row in enumerate(square):
        for c, val in enumerate(square_row):
            nr, nc = r + sr, c + sc
            # 벽이라면 내구도 깎임
            grid[nr][nc] = val - 1 if val > 0 else 0

    # square에 속하는 참가자도 회전
    for person in people:
        person.rotate(start, end)

    # 출구도 회전
    r, c = exit
    # square의 row 수
    row = er - sr + 1
    # square 내에서의 좌표
    nr, nc = r - sr, c - sc
    # square를 시계 방향으로 90도 돌렸을 때의 위치
    exit = (nc + sr, row - nr - 1 + sc)

def is_everyone_arrived():
    for person in people:
        if not person.arrived:
            return False
    return True

def get_exit():
    return (exit[0] + 1, exit[1] + 1)

def get_total_distance():
    d = 0

    for person in people:
        d += person.distance

    return d

if __name__ == "__main__":
    for _ in range(K):
        # 1. 참가자 움직이기
        for person in people:
            person.move()

        # 2. 움직인 결과, 모두가 출구에 도달했으면 즉시 종료 (중요!)
        if is_everyone_arrived():
            break

        # 3. 정사각형 찾기
        start, end = find_square()

        # 4. 정사각형 회전
        rotate_square(start, end, grid)

    print(get_total_distance())
    print(*get_exit())