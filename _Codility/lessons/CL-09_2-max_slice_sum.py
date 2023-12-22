# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
# https://app.codility.com/demo/results/training5AG789-ATZ/

def solution(A):
    # Kadane's algorithm
    prev = 0
    max_sum = -1e7

    for a in A:
        prev = max(prev + a, a)
        max_sum = max(max_sum, prev)

    return max_sum
