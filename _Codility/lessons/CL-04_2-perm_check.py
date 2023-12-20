# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
# https://app.codility.com/demo/results/training5PTTKR-G95/

def solution(A):
    candidates = set(range(1, len(A) + 1))

    for a in A:
        if a in candidates:
            candidates.remove(a)

    return 0 if candidates else 1
