# https://school.programmers.co.kr/learn/courses/30/lessons/67259

def solution(board):
    from collections import deque

    N = len(board)

    # 상 하 좌 우
    # TIP: 어차피 되돌아가는 경우는 없을테니 방향을 ("H", "V")가 아닌 (0, 1, 2, 3)로 두고, 이전 방향과 동일한지 여부를 판단해도 된다!
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    INF = int(1e9)

    def bfs(c, d, x, y):
        q = deque([(c, d, x, y)])  # (비용, 방향, x좌표, y좌표)
        result = [[INF] * N for _ in range(N)]
        result[x][y] = 0

        while q:
            c, d, x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # board[nx][ny]로의 새로운 비용 구하기
                new_c = c + (100 if i == d else 600)  # 방향이 같으면 100원 추가, 다르면 600원 추가

                # 범위 확인 & 벽이 아닌 곳 확인 & 더 적은 비용이면 업데이트
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and new_c < result[nx][ny]:
                    result[nx][ny] = new_c
                    q.append((new_c, i, nx, ny))

        return result[-1][-1]

    result = min(bfs(0, 1, 0, 0), bfs(0, 3, 0, 0))  # 방향: 0(상), 1(하), 2(좌), 우(3)

    return result
