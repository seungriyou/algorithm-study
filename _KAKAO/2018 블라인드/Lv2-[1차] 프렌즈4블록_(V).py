# https://school.programmers.co.kr/learn/courses/30/lessons/17679

# TIP: 블록 떨어뜨리기...!

def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    def get_removed_blocks():
        removed = set()

        # 2x2 사각형의 오른쪽 하단 블록을 기준으로,
        for i in range(1, m):
            for j in range(1, n):
                if (
                    # (1) 빈 블록이 아니면서
                    board[i][j] != "." and
                    # (2) 나머지 세 블록과 값이 같다면
                    board[i - 1][j - 1] == board[i - 1][j] == board[i][j - 1] == board[i][j]
                ):
                    # 지워질 블록에 2x2 사각형 내 모든 좌표 추가
                    removed |= {(i - 1, j - 1), (i - 1, j), (i, j - 1), (i, j)}

        return removed

    def drop_blocks():
        # row 별로 보기 (다음 row를 봐야하므로, 맨 밑에서 두번째 row 부터 거꾸로)
        for i in range(m - 2, -1, -1):
            # 해당 row에서 각 col 보기
            for j in range(n):
                k = i
                # 블록을 떨어뜨릴 row 번호 찾기 (board를 벗어나지 않고 비어있는 곳)
                while k + 1 < m and board[k + 1][j] == ".":
                    k += 1
                # 블록을 떨어뜨릴 다음 row를 찾았다면 떨어뜨리기!
                if k != i:
                    board[i][j], board[k][j] = board[k][j], board[i][j]

    def debug():
        # 디버깅용 board 출력 함수
        for row in board:
            print(row)
        print()

    # debug()

    while True:
        # (1) 지워질 블록의 좌표 모으기
        removed = get_removed_blocks()

        # (2) 더 이상 지워질 좌표가 없다면 종료
        if not removed:
            break

        # (3) answer 업데이트
        answer += len(removed)

        # (4) 블록 지우기
        for i, j in removed:
            board[i][j] = "."
        # debug()

        # (5) 블록 떨어뜨리기
        drop_blocks()
        # debug()

    return answer
