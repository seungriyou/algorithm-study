
key = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]
lock = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

def solution(key, lock):
    def rotate_by_90(original, m):
        rotated = [[0] * m for _ in range(m)]
        for r in range(m):
            for c in range(m):
                rotated[c][m - 1 - r] = original[r][c]
        return rotated

    def check(new_lock, m, n):
        for r in range(m - 1, m - 1 + n):
            for c in range(m - 1, m - 1 + n):
                if new_lock[r][c] != 1:
                    return False
        return True

    m = len(key)
    n = len(lock)

    # 확장한 new_lock 만들기 (중앙에 기존 lock)
    length = 2 * (m - 1) + n
    new_lock = [[0] * length for _ in range(length)]
    for i in range(n):
        for j in range(n):
            new_lock[i + m - 1][j + m - 1] = lock[i][j]

    # key를 rotate 하면서 진행
    for r in range(4):
        key = rotate_by_90(key, m)
        # key를 움직이면서 수행
        for k in range(m - 1 + n):
            for l in range(m - 1 + n):
                # 열쇠 넣기 (더하기)
                for i in range(m):
                    for j in range(m):
                        new_lock[i + k][j + l] += key[i][j]
                if check(new_lock, m, n):
                    return True
                # 열쇠 빼기 (빼기)
                for i in range(m):
                    for j in range(m):
                        new_lock[i + k][j + l] -= key[i][j]
    return False

print(solution(key, lock))
