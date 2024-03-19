# https://www.codetree.ai/training-field/frequent-problems/problems/cube-rounding-again

"""
dice = [1, 2, 3, 4, 5, 6]
    4
  3 0 2 5
    1       (index 기준)

격자판: n*n
주사위 굴리는 횟수: m번

주사위가 움직일 방향 (시계방향으로 90도씩) // index 변경 내역 (다중할당으로 dice 원소 swapping) // 위치 변위
    0: 우   /   3, 0, 2, 5  -> 5, 3, 0, 2   /   (0, 1)
    1: 하   /   4, 0, 1, 5  -> 5, 4, 0, 1   /   (1, 0)
    2: 좌   /   3, 0, 2, 5  -> 0, 2, 5, 3   /   (0, -1)
    3: 상   /   4, 0, 1, 5  -> 0, 1, 5, 4   /   (-1, 0)

===========

[이전 값] 주사위 방향 d(0, 1, 2, 3), 주사위 위치 r, c

[굴릴 때마다의 동작]
1. 주사위 옮기기 (w/ 방향)
    - 새로운 위치가 격자를 벗어난다면, 방향 반대로 업데이트 & 새로운 위치 다시 구하기   // get_direction_and_new_loc(direction, loc)
    - 주사위 굴리기 (index 변경)    // roll_dice(direction)
2. 주사위의 새로운 위치의 값과 (1) 상하좌우로 인접하며 (2) 같은 숫자가 적혀있는 모든 칸의 합만큼 점수 업데이트  // update_score(loc)
3. 다음 주사위 방향 업데이트    // get_next_direction(loc)
    - 주사위의 아랫면 > 보드의 해당 칸에 있는 숫자: 시계방향 회전
    - 주사위의 아랫면 < 보드의 해당 칸에 있는 숫자: 반시계방향 회전
    - 주사위의 아랫면 == 보드의 해당 칸에 있는 숫자: 방향 유지
"""


from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dice = [1, 2, 3, 4, 5, 6]

# 0: 우, 1: 하, 2: 좌, 3: 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def get_direction_and_new_loc(direction, r, c):
    # 방향 및 새로운 위치 구하기
    nr, nc = r + dr[direction], c + dc[direction]

    # 새로운 위치가 격자를 벗어난다면, 반대 방향으로 이동
    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        # (1) 방향 반대로 업데이트
        direction = (direction + 2) % 4
        # (2) 새로운 위치 다시 구하기
        nr, nc = r + dr[direction], c + dc[direction]

    return direction, nr, nc


def roll_dice(direction):
    if direction == 0:      # 우
        dice[3], dice[0], dice[2], dice[5] = dice[5], dice[3], dice[0], dice[2]

    elif direction == 1:    # 하
        dice[4], dice[0], dice[1], dice[5] = dice[5], dice[4], dice[0], dice[1]

    elif direction == 2:    # 좌
        dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]

    elif direction == 3:    # 상
        dice[4], dice[0], dice[1], dice[5] = dice[0], dice[1], dice[5], dice[4]


def update_score(r, c):
    val = grid[r][c]

    q = deque([(r, c)])
    visited = {(r, c)}
    cnt = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in visited or grid[nr][nc] != val:
                continue

            cnt += 1
            q.append((nr, nc))
            visited.add((nr, nc))

    return val * cnt


def get_next_direction(direction, r, c):
    if (bottom := dice[5]) > grid[r][c]:
        return (direction + 1) % 4

    elif bottom < grid[r][c]:
        return (direction + 3) % 4

    else:
        return direction


if __name__ == "__main__":
    d = r = c = 0
    score = 0

    for _ in range(m):
        # 1. 주사위 굴리기
        d, r, c = get_direction_and_new_loc(d, r, c)
        roll_dice(d)

        # 2. 점수 업데이트
        score += update_score(r, c)

        # 3. 새로운 방향 업데이트
        d = get_next_direction(d, r, c)

    print(score)
