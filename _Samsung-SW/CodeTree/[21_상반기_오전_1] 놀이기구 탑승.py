# https://www.codetree.ai/training-field/frequent-problems/problems/go-on-the-rides

n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
like_info = [set() for _ in range(n * n + 1)]
student_order = []
scores = [0, 1, 10, 100, 1000]

for _ in range(n * n):
    idx, *likes = map(int, input().split())

    student_order.append(idx)
    like_info[idx] |= set(likes)


def per_cell(r, c, student_idx):
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    like_num = empty_num = 0

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 1 <= nr <= n and 1 <= nc <= n:
            # 좋아하는 학생 수
            if board[nr][nc] in like_info[student_idx]:
                like_num += 1
            # 빈칸 수
            elif board[nr][nc] == 0:
                empty_num += 1

    return (-like_num, -empty_num, r, c)


for idx in student_order:
    min_result = (float("inf"), float("inf"), n + 1, n + 1)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] == 0:
                min_result = min(min_result, per_cell(i, j, idx))

    _, _, r, c = min_result
    board[r][c] = idx


score = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        t = per_cell(i, j, board[i][j])
        score += scores[-t[0]]

print(score)
