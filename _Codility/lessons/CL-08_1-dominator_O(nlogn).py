# https://app.codility.com/programmers/lessons/8-leader/dominator/
# https://app.codility.com/demo/results/trainingE3H5AT-KAK/

def solution(A):
    # if len(A) == 0, return -1
    if not A:
        return -1

    # sort A (using enumerate for idx)
    A = sorted(list((a, i) for i, a in enumerate(A)))

    # get middle element
    mid = len(A) // 2
    candidate = A[mid][0]

    # check if the candidiate is dominant
    idx = cnt = 0
    for a, i in A:
        if a == candidate:
            cnt += 1
            idx = i

    return idx if cnt > mid else -1
