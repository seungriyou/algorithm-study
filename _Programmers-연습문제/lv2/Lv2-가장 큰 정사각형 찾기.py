# https://school.programmers.co.kr/learn/courses/30/lessons/12905
# https://leetcode.com/problems/maximal-square/

def solution(board):
    """
    1D DP
        2D DP의 dp[i][j]에서 dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]만 확인하기 때문에,
        upper left인 dp[i - 1][j - 1]만 미리 저장해둔다면 1D DP로 space-optimize가 가능하다.
    """

    row, col = len(board), len(board[0])

    dp = [0] * (col + 1)
    max_len = upper_left = 0

    for i in range(row):
        for j in range(col):
            # 현재 보고 있는 위치가 1이라면
            if board[i][j] == 1:
                # 다음 j에서 사용할 upper_left 값 미리 저장해두기
                tmp = dp[j + 1]

                # 현재 dp 값 업데이트 (대각선 왼쪽 위, 위, 왼쪽)
                dp[j + 1] = min(upper_left, dp[j + 1], dp[j]) + 1

                # max_len, upper_left 업데이트
                max_len, upper_left = max(max_len, dp[j + 1]), tmp

            # 현재 보고 있는 위치가 1이 아니라면 0으로 초기화해야 함
            else:
                dp[j + 1] = upper_left = 0

    return max_len * max_len


def solution2(board):
    """
    2D DP
        - dp[i][j]: board[i - 1][j - 1]가 포함되는 1로 구성된 정사각형의 한 변의 최대 길이
        - 현재 보고 있는 [i][j] 위치의 (대각선 왼쪽 위, 위, 왼쪽)의 dp 값 중 최솟값에 1을 더해주면 된다.
    """

    row, col = len(board), len(board[0])

    dp = [[0] * (col + 1) for _ in range(row + 1)]
    max_len = 0

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if board[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_len = max(max_len, dp[i][j])

    return max_len * max_len
