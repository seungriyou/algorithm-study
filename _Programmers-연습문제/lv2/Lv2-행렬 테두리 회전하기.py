# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []

    mat = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]

    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

    def rotate(lr, lc, rr, rc):
        d = 0
        r, c = lr, lc
        min_val = prev = mat[lr + 1][lc]
        visited = set()

        while (r, c) not in visited:
            # prev <-> mat[r][c] swap
            mat[r][c], prev = prev, mat[r][c]

            # visited 기록
            visited.add((r, c))

            # 최솟값 업데이트
            min_val = min(min_val, prev)  # mat[r][c]

            # 위치 및 방향 업데이트
            nr, nc = r + dr[d], c + dc[d]
            if not (lr <= nr <= rr and lc <= nc <= rc):
                d = (d + 1) % 4
                nr, nc = r + dr[d], c + dc[d]
            r, c = nr, nc

        return min_val

    for lr, lc, rr, rc in queries:
        answer.append(rotate(lr - 1, lc - 1, rr - 1, rc - 1))

    return answer
