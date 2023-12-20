# https://app.codility.com/programmers/lessons/6-sorting/distinct/
# https://app.codility.com/demo/results/trainingGV6NF5-STM/

def solution(A):
    # return len(set(A))

    A.sort()

    visited = set()
    cnt = 0

    for a in A:
        if a not in visited:
            visited.add(a)
            cnt += 1

    return cnt
