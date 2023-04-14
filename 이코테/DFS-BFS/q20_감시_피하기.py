# https://www.acmicpc.net/problem/18428

from itertools import combinations

n = int(input())
board = [] # 복도 정보
teachers = [] # 선생님 위치 정보
blanks = [] # 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == "T":
            teachers.append((i, j))
        elif board[i][j] == "X":
            blanks.append((i, j))

# 선생님이 특정 방향으로 감시 진행 시, 학생 발견 여부
def is_discovered(x, y, direction):
    # 왼쪽으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == "S": # 학생이 있는 경우
                return True
            elif board[x][y] == "O": # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == "S": # 학생이 있는 경우
                return True
            elif board[x][y] == "O": # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == "S":  # 학생이 있는 경우
                return True
            elif board[x][y] == "O":  # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == "S":  # 학생이 있는 경우
                return True
            elif board[x][y] == "O":  # 장애물이 있는 경우
                return False
            x += 1
    # 학생과 장애물이 모두 없으면 False
    return False

# 장애물 설치 시마다 확인하는 프로세스
# True = 학생 발견, False = 학생 미발견
def process():
    # 모든 선생님들의 위치를 하나씩 확인
    for x, y in teachers:
        # 각 선생님마다 4가지 방향 검사
        for i in range(4):
            if is_discovered(x, y, i):
                return True
    return False

can_avoid = False # 학생들이 발견되지 않을 수 있는지의 여부

for to_add in combinations(blanks, 3):
    # 장애물 설치하기
    for x, y in to_add:
        board[x][y] = "O"
    # 학생을 발견하지 못한 경우, 학생들이 발견되지 않을 수 있다는 뜻이므로 break
    if not process():
        can_avoid = True
        break
    # 장애물 다시 빼기
    for x, y in to_add:
        board[x][y] = "X"

if can_avoid:
    print("YES")
else:
    print("NO")
