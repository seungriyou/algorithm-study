"""
- L*L 체스판
    - 0: 빈 칸
    - 1: 함정
    - 2: 벽
- 기사: N명
    - 초기 위치 (r, c)
    - 방패: (r, c)를 좌측 상단으로 하여 h*w 크기의 직사각형 형태
    - 체력 k
- 왕 명령: Q개
    - i번 기사에게 방향 d로 한 칸 이동하라는 명령
    - 이미 사라진 기사 번호가 주어질 수도 있음
    - d: 0, 1, 2, 3 = 상, 우, 하, 좌

- Q번의 대결이 모두 끝난 후 생존한 기사들이 받은 총 대미지의 합 출력

1. 기사 이동
    - 명령 받은 기사는 상하좌우 중 하나로 한 칸 이동
    - 이동하려는 위치에 다른 기사가 있다면, 그 기사도 함께 연쇄적으로 한 칸 밀림
    - 기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동할 수 없음
    - 체스판에서 사라진 기사에게 명령을 내리면 아무 반응이 없음

2. 대결 대미지
    - 밀려난 기사들은 피해를 입음
    - 해당 기사가 이동한 곳에서 w*h 직사각형 내에 놓여있는 함정의 수만큼만 피해를 입음
    - 각 기사마다 피해를 받은 만큼 체력이 깎임
    - 현재 체력 이상의 대미지를 받으면 체스판에서 사라짐
    - 명령을 받은 기사는 피해 입지 X
    - 기사들은 모두 밀린 후에 대미지 입음
    - 밀렸더라도, 해당 위치에 함정이 없다면 피해를 입지 X

[ Knight ]
- 값
    - r
    - c
    - h
    - w
    - k
    - disappeared
    - damage
- 동작
    - 자신에게 해당하는 모든 위치를 반환
    - 대미지
        - 대미지 계산
        - damage 업데이트
        - disappeared 업데이트
"""
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

L, N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)]
knights = [tuple(map(int, input().split())) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(Q)]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]


class Knight:
    def __init__(self, idx, r, c, h, w, k):
        self.idx = idx
        self.r = r
        self.c = c
        self.h = h
        self.w = w
        self.k = k
        self.disappeared = False
        self.damage = 0

    def __repr__(self):
        return f"<Knight #{self.idx}> loc={(self.r, self.c)} h={self.h} w={self.w} k={self.k} " \
               f"disappeared={self.disappeared} damage={self.damage}"

    def get_all_locs(self):
        for i in range(self.h):
            for j in range(self.w):
                yield self.r + i, self.c + j

    def get_damage(self):
        if self.disappeared:
            return

        for r, c in self.get_all_locs():
            if board[r][c] == 1:
                self.damage += 1

        if self.k <= self.damage:
            self.disappeared = True

    def move(self, d):
        self.r += dr[d]
        self.c += dc[d]

knights = [Knight(i + 1, r - 1, c - 1, h, w, k) for i, (r, c, h, w, k) in enumerate(knights)]

def move_and_get_pushed_knights(idx, d):
    moving_knight = knights[idx - 1]

    # 사라진 기사라면 곧바로 빈 set() return
    if moving_knight.disappeared:
        return set()

    # 사라지지 않은 기사들을 표시
    _knights = [[0] * L for _ in range(L)]
    for knight in knights:
        if not knight.disappeared:
            for r, c in knight.get_all_locs():
                _knights[r][c] = knight.idx

    # BFS
    visited = [[False] * L for _ in range(L)]
    q = deque([])
    pushed_knights = set()

    # 시작하는 기사의 모든 위치를 q에 넣고 visited 처리
    for r, c in moving_knight.get_all_locs():
        q.append((r, c))
        visited[r][c] = True

    while q:
        r, c = q.popleft()

        # 새로운 위치 구하기
        nr, nc = r + dr[d], c + dc[d]

        # board를 벗어났거나, 벽이 존재한다면 곧바로 빈 set() return
        if not (0 <= nr < L and 0 <= nc < L) or board[nr][nc] == 2:
            return set()

        # 새로운 위치에 다른 기사가 존재한다면, 해당하는 모든 위치를 q에 넣고 방문 처리
        if not visited[nr][nc] and (new_knight_idx := _knights[nr][nc]) and new_knight_idx not in pushed_knights:
            pushed_knights.add(new_knight_idx)
            for r, c in knights[new_knight_idx - 1].get_all_locs():
                q.append((r, c))
                visited[r][c] = True

    # 중단되지 않았다면, 기사 움직이기
    # NOTE: pushed_knights가 set()이어도, moving_knight는 밀릴 수 있는 경우가 있다!
    moving_knight.move(d)
    for idx in pushed_knights:
        knight = knights[idx - 1]
        knight.move(d)

    return pushed_knights


def get_damaged(pushed_knights):
    for idx in pushed_knights:
        knight = knights[idx - 1]
        knight.get_damage()


def get_total_damage():
    damage = 0
    for knight in knights:
        if not knight.disappeared:
            damage += knight.damage

    return damage


if __name__ == "__main__":
    for i, d in commands:
        pushed_knights = move_and_get_pushed_knights(i, d)
        if pushed_knights:
            get_damaged(pushed_knights)

    print(get_total_damage())
