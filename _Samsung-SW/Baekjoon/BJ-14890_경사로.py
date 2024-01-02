# https://www.acmicpc.net/problem/14890
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]


def is_possible(line: list[int]) -> bool:
    """
    입력으로 들어오는 line은 int로 이루어진 1차원 리스트로 간주

    1. 이전 칸과의 높이 차이가 1보다 크면 종료
    2. 이미 slide가 설치되어 있으면 넘어가기
    3-1. 이전 < 현재: 경사로 놓기 위해 **이전 칸 기준으로** 왼쪽으로 L칸 검사
    3-2. 이전 > 현재: 경사로 놓기 위해 오른쪽으로 L칸 검사
    """

    # 각 index에 경사로 설치 여부 트래킹
    slide = [False] * N

    for j in range(1, N):
        # 1. 이전 칸과의 높이 차이가 1보다 크면 종료
        if abs(line[j] - line[j - 1]) > 1:
            return False

        # 2. 이미 slide가 설치되어 있으면 넘어가기
        if slide[j]:
            continue

        # 3-1. 이전 < 현재: 경사로 놓기 위해 **이전 칸 기준으로** 왼쪽으로 L칸 검사
        if line[j - 1] < line[j]:
            for k in range(L):
                # (1) 범위가 넘어가거나 (2) 이미 slide가 설치되어 있거나 (3) 높이가 일정하지 않은 경우 종료
                if j - k - 1 < 0 or slide[j - k - 1] or line[j - k - 1] != line[j - 1]:
                    return False
                # slide 설치
                slide[j - k - 1] = True

        # 3-2. 이전 > 현재: 경사로 놓기 위해 오른쪽으로 L칸 검사
        elif line[j - 1] > line[j]:
            for k in range(L):
                # (1) 범위가 넘어가거나 (2) 높이가 일정하지 않은 경우 종료
                if j + k >= N or line[j + k] != line[j]:
                    return False
                # slide 설치
                slide[j + k] = True

    return True


cnt = 0

# row 확인
for i in range(N):
    if is_possible(map[i]):
        cnt += 1

# column 확인
for i in range(N):
    if is_possible([map[j][i] for j in range(N)]):
        cnt += 1

print(cnt)
