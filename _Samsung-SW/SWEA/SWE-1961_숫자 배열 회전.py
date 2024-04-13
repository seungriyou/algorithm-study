# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def rotate90(mat):
    mat = list(zip(*mat[::-1]))
    return mat

def get_result(mat):
    mat90 = rotate90(mat)
    mat180 = rotate90(mat90)
    mat270 = rotate90(mat180)

    for r90, r180, r270 in zip(mat90, mat180, mat270):
        lst = ["".join(map(str, r90)), "".join(map(str, r180)), "".join(map(str, r270))]
        print(*lst)


if __name__ == "__main__":
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        print(f"#{test_case}")
        N = int(input())
        mat = [list(map(int, input().split())) for _ in range(N)]
        get_result(mat)
