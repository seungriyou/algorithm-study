# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []

    triangle = [[0] * n for _ in range(n)]
    dr, dc = [1, 0, -1], [0, 1, -1]  # 방향은 [아래, 오른쪽, 왼쪽 대각선]으로 세 가지

    d = 0  # 첫 방향은 아래
    r = c = 0  # 첫 시작은 (0, 0)
    i = 1
    tot = n * (n + 1) // 2

    while i <= tot:
        # 기록
        triangle[r][c] = i
        i += 1

        # nr, nc 구하기
        nr, nc = r + dr[d], c + dc[d]
        # nr, nc이 범위를 벗어났거나 이미 방문한 곳이라면 방향 전환하기
        if nr >= n or nc >= n or triangle[nr][nc] != 0:
            d = (d + 1) % 3
            nr, nc = r + dr[d], c + dc[d]

        # 좌표 업데이트
        r, c = nr, nc

    # answer에 모으기
    for row, c in zip(triangle, range(1, n + 1)):
        answer.extend(row[:c])

    return answer
