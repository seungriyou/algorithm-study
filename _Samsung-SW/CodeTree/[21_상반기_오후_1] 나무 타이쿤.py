# https://www.codetree.ai/training-field/frequent-problems/problems/tree-tycoon

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
moving = [tuple(map(int, input().split())) for _ in range(m)]

# 특수 영양제 위치
loc = {(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)}

# 이동 방향 (r, c) (→ ↗ ↑ ↖ ← ↙ ↓ ↘)
dd = [None, (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]


def move(d, p, loc):
    """
    input: d = 이동 방향, p = 칸 수, loc = 특수 영양제 좌표
    output: 이동 후 특수 영양제 좌표
    """
    new_loc = set()

    dr, dc = dd[d][0] * p, dd[d][1] * p

    for r, c in loc:
        nr, nc = (r + dr + n) % n, (c + dc + n) % n
        new_loc.add((nr, nc))

    return new_loc


def grow(loc):
    # 1. 영양제 위치마다 1 증가
    for r, c in loc:
        grid[r][c] += 1

    # 2. 4방향 대각선 (** 주의! 확인하면서 바로 grid 값 업데이트 하면 X **)
    diag = []
    for r, c in loc:
        cnt = 0
        for i in [2, 4, 6, 8]:
            dr, dc = dd[i]
            nr, nc = r + dr, c + dc

            # 범위 벗어나면 X
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            # 높이가 1 이상인 리브로수의 개수만큼 높이 증가
            if grid[nr][nc] >= 1:
                cnt += 1
        diag.append((r, c, cnt))

    for r, c, cnt in diag:
        grid[r][c] += cnt


def cut_and_get_new_loc(loc):
    new_loc = set()

    for i in range(n):
        for j in range(n):
            # (1) 해당 년도에 특수 영양제를 맞은 땅이 아니고 (2) 높이가 2 이상인 리브로수 자르고, 새로운 위치로 추가
            if (i, j) not in loc and grid[i][j] >= 2:
                grid[i][j] -= 2
                new_loc.add((i, j))

    return new_loc


def get_total_height():
    total_height = 0
    for i in range(n):
        for j in range(n):
            total_height += grid[i][j]
    return total_height


if __name__ == "__main__":
    for d, p in moving:
        # 1. 특수 영양제가 이동한 새로운 좌표 구하기
        loc = move(d, p, loc)

        # 2. 리브로수 자라기
        grow(loc)

        # 3. 리브로수를 조건에 맞게 자르고, 새로운 특수 영양제 위치 구하기
        loc = cut_and_get_new_loc(loc)

    print(get_total_height())
