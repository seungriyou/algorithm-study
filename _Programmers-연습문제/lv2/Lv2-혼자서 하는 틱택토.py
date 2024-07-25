# https://school.programmers.co.kr/learn/courses/30/lessons/160585

def solution(board):
    """
    다음의 조건 중 하나 이상에 해당하면 return 0:
        1. O 개수가 X 개수보다 적거나, (O 개수 - X 개수) > 1 (turn의 총 개수가 짝수이면 0, 홀수이면 1이어야 하고, 홀수인 경우엔 O가 한 번 더)
        2. O win && X win (O와 X가 둘다 이길 수는 없음)
        3. O win && (0 개수 - X 개수) != 1 (O가 이겼는데도 X가 한 번 더 진행한 것이므로)
        4. X win && (O 개수 - X 개수) != 0 (X가 이겼는데도 O가 한 번 더 진행한 것이므로)
    """

    def check_win(player):
        # 가로
        for row in board:
            if row[0] == player and len(set(row)) == 1:
                return True
        # 세로
        for col in zip(*board):
            if col[0] == player and len(set(col)) == 1:
                return True
        # 대각선 (2개)
        if board[1][1] == player and (
                board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
            return True

        return False

    # O와 X의 개수 세기
    cnt_O = cnt_X = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == "O":
                cnt_O += 1
            elif board[r][c] == "X":
                cnt_X += 1

    # 1. O의 개수 & X의 개수 비교
    if not (cnt_O == cnt_X or cnt_O == cnt_X + 1):
        return 0

    won_O, won_X = check_win("O"), check_win("X")

    # 2. O와 X가 모두 승리한 경우
    if won_O and won_X:
        return 0
    # 3. O win && (0 개수 - X 개수) != 1
    elif won_O and cnt_O != cnt_X + 1:
        return 0
    # 4. X win && (O 개수 - X 개수) != 0
    elif won_X and cnt_O != cnt_X:
        return 0

    return 1
