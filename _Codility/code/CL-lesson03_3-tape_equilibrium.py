# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# https://app.codility.com/demo/results/trainingFKNHUB-HYT/

def solution(A):
    left, right = A[0], sum(A) - A[0]
    min_diff = abs(left - right)

    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        min_diff = min(min_diff, abs(left - right))

    return min_diff
