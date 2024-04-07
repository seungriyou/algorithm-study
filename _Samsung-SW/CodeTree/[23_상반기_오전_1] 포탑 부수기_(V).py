"""
- 격자: N*M (모든 위치에 포탑 존재)
- 포탑: N*M
    - 공격력
        - 줄어들거나, 늘어나거나
        - 공격력이 0 이하가 된다면 해당 포탑은 부서지며 더 이상 공격 X
        - 최초에 공격력이 0인, 즉 부서진 포탑이 존재할 수 있음
- 턴: K번
- 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지

[ 하나의 턴 ]
1.  공격자 선정
    - 부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정된다. 이때, 공격자는 N+M 만큼의 공격력이 증가된다.
    - 가장 약한 포탑:
        1) 공격력이 가장 낮은 포탑
        2) 1)이 여러 개면, 가장 최근에 공격한 포탑 (모든 포탑은 시점 0에 모두 공격했다고 가정)
        3) 2)가 여러 개면, 각 포탑 위치의 행과 열의 합이 가장 큰 포탑
        4) 3)이 여러 개면, 각 포탑 위치의 열 값이 가장 큰 포탑

2.  공격자의 공격
    선정된 공격자는 자신을 제외한 가장 강한 포탑을 공격한다.
    - 가장 강한 포탑:
        1) 공격력이 가장 높은 포탑
        2) 1)이 여러 개면, 공격한지 가장 오래된 포탑 (모든 포탑은 시점 0에 모두 공격했다고 가정)
        3) 2)가 여러 개면, 각 포탑 위치의 행과 열의 합이 가장 작은 포탑
        4) 3)이 여러 개면, 각 포탑 위치의 열 값이 가장 작은 포탑

    레이저 공격을 먼저 시도하고, 안되면 포탄 공격을 한다.
    - 레이저 공격 (공격자 ~ 공격 대상 포탑까지의 최단 경로)
        1) 상하좌우 4개의 방향으로 움직일 수 있다.
        2) 부서진 포탑이 있는 위치는 지날 수 없다.
        3) 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나온다.
        4) 길이가 동일한 최단 경로가 2개 이상이면, 우/하/좌/상의 우선순위대로 먼저 움직인 경로가 선택된다.
        5) 피해
            - 공격 대상: 공격자의 공격력만큼 피해 입힘
            - 레이저 경로에 있는 포탑: 공격자 공격력의 절반만큼 피해 입힘
    - 포탄 공격 (레이저 공격이 가능한 경로가 없는 경우)
        1) 피해:
            - 공격 대상: 공격자의 공격력만큼 피해 입힘
            - 주위 8개 방향의 포탑: 공격자 공격력의 절반만큼 피해 입힘
                * 공격자는 해당 공격에 영향 받지 X
            - 가장자리에 포탄이 떨어졌다면, 추가 피해가 반대편 격자에 미침

3. 포탑 부서짐
    - 공격력이 0 이하가 된 포탑은 부서진다.

4. 포탑 정비
    - 부서지지 않은 포탑 중 공격과 무관했던 포탑은 공격력 +1
    - 공격과 무관 = 공격자도 X, 공격에 의해 피해받지도 X


[ 격자 ]
- 0: 부서진 포탑
- 나머지: 공격이 가능한 포탑

[ last_attack ]
- 초깃값: 0
- 공격대상이 될 때마다 update

[ 필요한 동작 ]
- select_weakest(): 가장 약한 포탑 고르기
    - input: k (공격한 턴 수)
    - output: (r, c)
    - 공격자는 N+M 만큼의 공격력이 증가
    - 공격자가 정해지면 last_attack를 k로 업데이트

- select_strongest(): 가장 강한 포탑 고르기
    - output: (r, c)

- _laser_attack(): 레이저 공격
    - input: 공격자 (r, c), 공격 대상자 (r, c)
    - output: bool
        - False: 레이저 공격이 가능한 경로가 없는 경우 -> _bomb_attack()
        - True: 레이저 공격이 가능하여 피해를 입히고, True 반환

- _bomb_attack(): 포탄 공격
    - input: 공격자 (r, c), 공격 대상자 (r, c)

- attack(): 공격하기
    - input: 공격자 (r, c), 공격 대상자 (r, c)
    1) 레이저 공격 시도하고, 안 되면 (False 라면)
    2) 포탄 공격

- destroy(): 포탑 부서지기
    - 0 이하가 된 것들을 모두 0 처리

- rearrange(): 포탑 정비
    - 공격과 무관한 && 0이 아닌 포탑을 ++

- is_only_one_remained(): 부서지지 않은 포탑의 개수가 1인지 확인하는 동작 (1이라면 중지)

- get_strongest(): 남아있는 포탑 중 가장 강한 포탑의 공격력을 반환하는 동작

[ 각 턴 ]
for k in range(K):
    # 1. related
    related = [[False] * M for _ in range(N)]
    # 2. 공격자 & 공격 대상자 고르기
    attacker, attacked = select_attacker_and_attacked(related)
    # 3. 공격하기
    attack(attacker, attacked, related)
    # 4. 포탑 부서지기
    destroy()
    # 5. 포탑 정비
    rearrange(related)

    # 부서지지 않은 포탑의 개수가 1이라면 중지
    if is_only_one_remained():
        break

get_strongest()
"""

from collections import deque

N, M, K = map(int, input().split())
grid =[list(map(int, input().split())) for _ in range(N)]
last_attack = [[0] * M for _ in range(N)]

def modify_loc(r, c):
    # r, c가 격자 내에 있으면 그대로 return
    if 0 <= r < N and 0 <= c < M:
        return (r, c)
    # 아니라면
    return ((r + N) % N, (c + M) % M)

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]


def select_attacker_and_attacked(related, k):
    candidates = []  # (공격력, -가장 최근에 공격한 턴 수, -(행+열), -열)

    # 부서지지 않은 포탑에 대해 모으기
    for r in range(N):
        for c in range(M):
            if grid[r][c]:
                candidates.append((grid[r][c], -last_attack[r][c], -(r + c), -c))

    # 내림차순 정렬
    candidates.sort()

    # attacker: weakest
    weakest = candidates[0]
    attacker = (weakest[3] - weakest[2], -weakest[3])


    # attacked: strongest
    strongest = candidates[-1]
    attacked = (strongest[3] - strongest[2], -strongest[3])

    # related에 표시
    related[attacker[0]][attacker[1]] = True
    related[attacked[0]][attacked[1]] = True

    # attacker 추가 동작
    # (1) 공격력 증가
    grid[attacker[0]][attacker[1]] += N + M
    # (2) 최근 공격 턴 수 기록
    last_attack[attacker[0]][attacker[1]] = k

    return attacker, attacked

def _laser_attack(attacker, attacked, related):
    """
    - 레이저 공격 (공격자 ~ 공격 대상 포탑까지의 최단 경로)
        1) 상하좌우 4개의 방향으로 움직일 수 있다.
        2) 부서진 포탑이 있는 위치는 지날 수 없다.
        3) 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나온다.
        4) 길이가 동일한 최단 경로가 2개 이상이면, 우/하/좌/상의 우선순위대로 먼저 움직인 경로가 선택된다.
        5) 피해
            - 공격 대상: 공격자의 공격력만큼 피해 입힘
            - 레이저 경로에 있는 포탑: 공격자 공격력의 절반만큼 피해 입힘
    """
    sr, sc = attacker

    # TODO: BFS에서 path 기록하는 방법 주의!
    q = deque([(sr, sc, [])])   # (r, c, path)
    visited = [[False] * M for _ in range(N)]
    visited[sr][sc] = True

    damage = grid[sr][sc]
    half_damage = damage // 2

    while q:
        r, c, path = q.popleft()

        # attacked에 도달한 경우
        if (r, c) == attacked:
            # 공격 대상에는 공격자의 공격력만큼 피해
            er, ec = path.pop()
            grid[er][ec] -= damage
            # path에 있는 포탑에는 공격력의 절반만큼 피해
            for pr, pc in path:
                grid[pr][pc] -= half_damage
                # related 표시
                related[pr][pc] = True
            return True

        for i in range(4):
            nr, nc = modify_loc(r + dr[i], c + dc[i])
            if not visited[nr][nc] and grid[nr][nc]:
                q.append((nr, nc, path + [(nr, nc)]))
                visited[nr][nc] = True

    return False

def _bomb_attack(attacker, attacked, related):
    """
    - 공격 대상: 공격자의 공격력만큼 피해 입힘
    - 주위 8개 방향의 포탑: 공격자 공격력의 절반만큼 피해 입힘
        * 공격자는 해당 공격에 영향 받지 X
    - 가장자리에 포탄이 떨어졌다면, 추가 피해가 반대편 격자에 미침
    """
    sr, sc = attacker
    er, ec = attacked

    damage = grid[sr][sc]
    half_damage = damage // 2

    # 공격 대상
    grid[er][ec] -= damage

    # 주위 8개 방향
    ddr, ddc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(8):
        nr, nc = modify_loc(er + ddr[i], ec + ddc[i])
        # 부서진 포탑이 아니고, 공격자가 아니어야 영향 받음
        if grid[nr][nc] and (nr, nc) != attacker:
            grid[nr][nc] -= half_damage
            related[nr][nc] = True


def attack(attacker, attacked, related):
    """
    - input: 공격자 (r, c), 공격 대상자 (r, c)
    1) 레이저 공격 시도하고, 안 되면 (False 라면)
    2) 포탄 공격
    """
    if not _laser_attack(attacker, attacked, related):
        _bomb_attack(attacker, attacked, related)


def destroy():
    """
    - 0 이하가 된 것들을 모두 0 처리
    """
    for i in range(N):
        for j in range(M):
            if grid[i][j] < 0:
                grid[i][j] = 0

def rearrange(related):
    """
    - 공격과 무관한 && 0이 아닌 포탑을 ++
    """
    for i in range(N):
        for j in range(M):
            if grid[i][j] and not related[i][j]:
                grid[i][j] += 1

def is_only_one_remained():
    """
    부서지지 않은 포탑의 개수가 1인지 확인하는 동작 (1이라면 중지)
    """
    cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                cnt += 1
                if cnt > 1:
                    return False
    return cnt == 1

def get_strongest():
    """
    남아있는 포탑 중 가장 강한 포탑의 공격력을 반환하는 동작
    """
    max_power = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] > max_power:
                max_power = grid[i][j]

    return max_power

def print_related():
    for row in related:
        print(*row)

def print_grid():
    for row in grid:
        print(*row)

if __name__ == "__main__":
    for k in range(1, K + 1):
        # 1. related
        related = [[False] * M for _ in range(N)]

        # 2. 공격자 & 공격 대상자 고르기
        attacker, attacked = select_attacker_and_attacked(related, k)

        # 3. 공격하기
        attack(attacker, attacked, related)

        # 4. 포탑 부서지기
        destroy()

        # 5. 포탑 정비
        rearrange(related)

        # 부서지지 않은 포탑의 개수가 1이라면 중지
        if is_only_one_remained():
            break

    print(get_strongest())
