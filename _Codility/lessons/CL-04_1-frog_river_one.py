# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# https://app.codility.com/demo/results/training5XVCSU-YH8/

def solution(X, A):
    waiting_leaves = set(range(1, X + 1))

    for i, a in enumerate(A):
        if a in waiting_leaves:
            waiting_leaves.remove(a)
        if not waiting_leaves:
            return i

    return -1
