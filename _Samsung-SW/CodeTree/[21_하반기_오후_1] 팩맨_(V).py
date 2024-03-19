# https://www.codetree.ai/training-field/frequent-problems/problems/pacman

"""
m: 몬스터 개수
t: 진행되는 턴의 수

pr, pc: 팩맨 초기 위치 (번째)
r, c, d: 몬스터의 위치, 방향 정보

d: 방향   [↑, ↖, ←, ↙, ↓, ↘, →, ↗]
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, -1, -1, -1, 0, 1, 1, 1]

[ 한 번의 턴 ]
    1. 몬스터 복제 시도
        - 몬스터의 현재 위치 & 같은 방향을 가진 몬스터 복제
        - 알 부화 시 깨어남

    2. 몬스터 이동 (위치 & 방향 변함)
        - 몬스터는 자신의 방향대로 한 칸 이동
            - 이동하려는 위치가 다음의 조건 중 하나에라도 해당되면 반시계 방향 45도 회전하며 판단
                (1) 새로운 위치에 몬스터 시체
                (2) 새로운 위치에 팩맨
                (3) 격자를 벗어남
            - 8방향 다 돌았음에도 불구하고 움직일 수 없다면 이동 X

    3. 팩맨 이동
        - 총 3칸 이동 & 각 이동마다 상하좌우 4가지 방향 -> 총 64개의 방법
        - 방법을 고르는 우선순위
            (1) 몬스터를 가장 많이 먹을 수 있는 방향으로 이동 (max_monster)
            (2) (1)이 여러 개라면 상-좌-하-우           (0-1-2-3)
        - 격자 밖으로 나가는 방법은 X

        - 칸에 있는 몬스터를 먹으면 몬스터의 시체 남기기
        - 알은 먹지 X
        - 움직이기 전에 함께 있었던 몬스터도 먹지 X

    4. 몬스터 시체 소멸
        - 몬스터의 시체는 2턴 동안만 유지

    5. 몬스터 복제 완성
        - 알 형태였던 몬스터 부화

[ 가져가야 할 것 ]
- 현재 턴에서의 살아있는 몬스터: 위치, 방향
- 몬스터 복제 (부화 전): 위치, 방향
- 팩맨: 위치
- 몬스터 시체: 위치, 방향, 생성된 턴
"""

from collections import deque

m, t = map(int, input().split())    # m: 몬스터 마리 수, t: 턴의 수
pr, pc = map(int, input().split())  # 팩맨의 초기 위치
pr -= 1
pc -= 1

alive_monsters = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(m):
    r, c, d = map(int, input().split())
    alive_monsters[r - 1][c - 1].append(d - 1)

dead_monsters = [[0] * 4 for _ in range(4)]

dead_monster_q = deque([[] for _ in range(2)])


def is_valid_loc(r, c):
    if 0 <= r < 4 and 0 <= c < 4:
        return True
    return False

def get_new_loc_and_d(r, c, d):
    #    [↑, ↖, ←, ↙, ↓, ↘, →, ↗]
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, -1, -1, -1, 0, 1, 1, 1]

    for i in range(8):
        nd = (d + i) % 8
        nr, nc = r + dr[nd], c + dc[nd]

        if not is_valid_loc(nr, nc) or dead_monsters[nr][nc] or (nr, nc) == (pr, pc):
            continue

        return nr, nc, nd

    return r, c, d

def move_packman(alive_monsters, r, c):
    # 상-좌-하-우 순서이므로, 반대로 탐색
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

    max_dead_monster = []
    npr, npc = -1, -1
    max_cnt = -1
    tmp = []
    visited = []

    def dfs(move, r, c, cnt):
        nonlocal npr, npc, max_cnt, max_dead_monster

        # base condition
        if move == 3:
            if max_cnt <= cnt:
                max_dead_monster = tmp[:]
                max_cnt = cnt
                npr, npc = r, c
            return

        # recur
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if is_valid_loc(nr, nc):
                # [주의] 이미 현재 path에서 거쳐간 곳이라면, monster를 먹었을 것이므로!
                n = len(alive_monsters[nr][nc]) if (nr, nc) not in visited else 0
                tmp.append((nr, nc, n))
                visited.append((nr, nc))

                dfs(move + 1, nr, nc, cnt + n)

                tmp.pop()
                visited.pop()

    dfs(0, r, c, 0)

    return max_dead_monster, npr, npc

def count_alive_monsters():
    alive_monsters_cnt = 0
    for r in range(4):
        for c in range(4):
            alive_monsters_cnt += len(alive_monsters[r][c])

    return alive_monsters_cnt


if __name__ == "__main__":
    for tn in range(t):
        # 1. 몬스터 복제
        alive_monsters_new = [[[] for _ in range(4)] for _ in range(4)]

        # 2. 몬스터 이동
        for r in range(4):
            for c in range(4):
                for d in alive_monsters[r][c]:
                    nr, nc, nd = get_new_loc_and_d(r, c, d)
                    alive_monsters_new[nr][nc].append(nd)

        # 3. 팩맨 이동 및 몬스터 죽이기
        dead_monster_new, pr, pc = move_packman(alive_monsters_new, pr, pc)

        for r, c, n in dead_monster_new:
            dead_monsters[r][c] += n
            alive_monsters_new[r][c] = []

        # 4. 몬스터 시체 소멸
        dead_monster_remove = dead_monster_q.popleft()
        dead_monster_q.append(dead_monster_new)

        for r, c, n in dead_monster_remove:
            dead_monsters[r][c] -= n

        # 5. 몬스터 복제 완성
        for r in range(4):
            for c in range(4):
                alive_monsters[r][c] += alive_monsters_new[r][c]

    # 살아남은 몬스터 개수 구하기
    print(count_alive_monsters())
