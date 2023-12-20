# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# https://app.codility.com/demo/results/training6V83NT-9C5/

def solution(A, K):
    # A == []일 때
    if not A:
        return A

    start = K % len(A)
    return A[-start:] + A[:-start]