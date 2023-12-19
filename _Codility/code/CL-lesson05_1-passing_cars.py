# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
# https://app.codility.com/demo/results/trainingGSNCG7-Z6S/

def solution(A):
    A += [0]
    cnt = 0

    for i in range(len(A) - 2, -1, -1):
        if A[i] == 0:
            cnt += A[i + 1]

        A[i] += A[i + 1]

    return -1 if cnt > 1_000_000_000 else cnt
