# https://app.codility.com/programmers/lessons/6-sorting/triangle/
# https://app.codility.com/demo/results/training4V4G46-X5Y/

def solution(A):
    A.sort()

    # A가 오름차순 정렬되어 있으므로, A[P] + A[Q] > A[R]이 True라면 나머지 조건도 True
    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0
