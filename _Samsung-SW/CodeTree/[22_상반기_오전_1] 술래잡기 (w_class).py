# https://www.codetree.ai/training-field/frequent-problems/problems/hide-and-seek

"""
[ 주어진 값 ]
- n*n : 격자
- m: 도망자
    - 이동 유형: 좌우 (1 / 오른쪽 보고 시작) / 상하 (2 / 아래쪽 보고 시작)
    - 시작 시점
    - 방향
- h: 나무
- k: 턴 수


[ 각 턴의 동작 ]
1. 도망자가 동시에 움직인다.
    - 술래와의 거리가 3이하인 도망자만 이동 (거리 = |x1 - x2| + |y1 - y2|)
    - 이동 규칙 (방향으로 1칸 이동)
        (1) 격자 벗어나지 않는 경우
            - 술래가 있다면 이동 X
            - 술래가 없다면 이동 O (나무 있어도 ok)
        (2) 격자 벗어나는 경우
            - 방향 반대로 틀기
            - 바뀐 방향으로 1칸 이동해도 해당 위치에 술래가 없다면 이동 O


2. 술래가 움직인다.
    - 달팽이 모양으로 이동 (한 턴에 1칸)
    - 이동 후의 위치가 이동 방향이 틀어지는 지점이라면, 방향 바로 틀기 (양 끝인 (1, 1) 혹은 (정중앙) 에서도 바로 틀어줘야 함)

3. 술래가 도망자를 잡는다.
    - 다음의 조건을 모두 만족하는 도망자를 잡는다.
        (1) 술래의 시야 내 3칸 이내
        (2) 나무가 있는 칸이 아닌 곳
    - 점수는, t(턴 수) * (잡힌 도망자의 수) 만큼 얻는다.
    - 잡힌 도망자는 사라진다.
"""

n, m, h, k = map(int, input().split())
runners = [tuple(map(int, input().split())) for _ in range(m)]
trees = {tuple(map(lambda x: x - 1, map(int, input().split()))) for _ in range(h)}

# 방향: 0, 1, 2, 3 = 상, 우, 하, 좌
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


def get_shifted_locs(n):
    r, c = n // 2, n // 2
    d = 0
    result = set()

    for i in range(1, n):
        for _ in range(2):
            r, c = r + dr[d] * i, c + dc[d] * i
            d = (d + 1) % 4
            result.add((r, c))

    return result


class Runner:
    def __init__(self, idx, r, c, d):
        self.idx = idx
        self.r = r
        self.c = c
        self.d = d

    def __repr__(self):
        return f"[Runner id={self.idx}] r={self.r} / c={self.c} / d={self.d}"

    def _get_distance(self, cr, cc):
        return abs(cr - self.r) + abs(cc - self.c)

    def move(self, cr, cc):
        """
        (1) 격자 벗어나지 않는 경우
            - 술래가 있다면 이동 X
            - 술래가 없다면 이동 O (나무 있어도 ok)
        (2) 격자 벗어나는 경우
            - 방향 반대로 틀기
            - 바뀐 방향으로 1칸 이동해도 해당 위치에 술래가 없다면 이동 O
        """
        # 자신과 술래의 거리가 3 이하인지 확인하고, 아니라면 넘어가기
        if self._get_distance(cr, cc) > 3:
            return

        # 새로운 위치 구하기
        nr, nc = self.r + dr[self.d], self.c + dc[self.d]

        # 격자 벗어나지 않는 경우
        if is_valid(nr, nc):
            # 술래가 없다면 이동
            if not (nr == cr and nc == cc):
                self.r, self.c = nr, nc
        # 격자 벗어나는 경우
        else:
            self.d = (self.d + 2) % 4  # 방향 반대로
            nr, nc = self.r + dr[self.d], self.c + dc[self.d]
            # 술래가 없다면 이동
            if not (nr == cr and nc == cc):
                self.r, self.c = nr, nc


class Catcher:
    def __init__(self, r=n // 2, c=n // 2, d=0, score=0, clock_wise=True):
        self.r = r
        self.c = c
        self.d = d
        self.score = score
        self.clock_wise = clock_wise

    def __repr__(self):
        return f"[Catcher] r={self.r} / c={self.c} / d={self.d} / score={self.score}"

    def move(self, should_be_shifted):
        # 새로운 위치 구하기
        self.r, self.c = self.r + dr[self.d], self.c + dc[self.d]

        # 새로운 위치가 방향이 변경되어야 하는 좌표면 방향 변경
        # (1) 양 끝점에 해당하면 완전 반대로
        if (nloc := (self.r, self.c)) in {(n // 2, n // 2), (0, 0)}:
            self.d = (self.d + 2) % 4
            self.clock_wise = not self.clock_wise

        # (2) 그 사이라면 시계/반시계 방향으로 90도씩
        elif nloc in should_be_shifted:
            self.d = (self.d + 1) % 4 if self.clock_wise else (self.d + 3) % 4

    def _get_range(self, trees):
        # [주의] 하나의 칸에 술래, 도망자, 나무가 함께 있으면, 술래는 도망자를 잡지 못 한다!!! (이것 때문에 삽질함)
        # 현재 방향으로 3칸 이내의 좌표 중, 나무가 없는 좌표 반환
        r, c = self.r, self.c
        result = set()

        for _ in range(3):
            # 좌표가 유효하지 않다면 중단
            if not is_valid(r, c):
                break
            # 해당 좌표에 나무가 없는 경우, 모으기
            if (r, c) not in trees:
                result.add((r, c))
            # 한 칸 전진
            r, c = r + dr[self.d], c + dc[self.d]

        return result

    def catch(self, runners, turn):
        # 나무가 없는 3칸 이내의 좌표 찾기
        _range = self._get_range(trees)

        # 해당 좌표에 해당하는 도망자가 있다면, 잡기
        removed = []
        for i, runner in runners.items():
            if (runner.r, runner.c) in _range:
                removed.append(i)
        for i in removed:
            del runners[i]

        # 점수 올리기
        self.score += (turn + 1) * len(removed)


if __name__ == "__main__":
    runners_dict = {i: Runner(i, r - 1, c - 1, d) for i, (r, c, d) in enumerate(runners)}
    catcher = Catcher()
    should_be_shifted = get_shifted_locs(n)

    for turn in range(k):
        # 0. 술래 위치
        cr, cc = catcher.r, catcher.c

        # 1. 도망자 이동
        for i, runner in runners_dict.items():
            runner.move(cr, cc)

        # 2. 술래 이동
        catcher.move(should_be_shifted)

        # 3. 도망자 잡기
        catcher.catch(runners_dict, turn)

    print(catcher.score)
