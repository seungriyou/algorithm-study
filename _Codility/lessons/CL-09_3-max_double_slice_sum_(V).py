# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
# https://app.codility.com/demo/results/trainingYM6B6Q-FTA/

def solution(A):
    """
    - 양 끝의 원소는 제외해도 된다.
    - 양 끝에서부터 max subarray sum을 각각 구한 후, y를 이동시켜가며 최대 값을 구하면 된다.
    - (X, Y, Z)가 (3, 4, 5)처럼 연속된 값이라면, 전체 원소가 음수여도 max_sum 값으로 0이 확보된다는 것이 핵심이다!
    """

    N = len(A)
    left = [0] * N  # left[i]: A[i]로 끝나는 subarray의 max sum
    right = [0] * N  # right[i]: A[i]로 시작하는 subarray의 max sum

    for i in range(1, N - 1):
        left[i] = max(left[i - 1] + A[i], 0)  # left[i - 1] + A[i]가 음수라면, A[i] 포함 이전 값들은 아예 보지 않도록 한다.

    for i in range(N - 2, 0, -1):
        right[i] = max(right[i + 1] + A[i], 0)  # right[i + 1] + A[i]가 음수라면, A[i] 포함 이후 값들은 아예 보지 않도록 한다.

    # max_sum의 최솟값은 0으로 설정한다.
    # (ex. (X, Y, Z)가 (3, 4, 5)처럼 연속된 값이라면, 전체 원소가 음수라도 max_sum 값으로 0은 확보된다.)
    max_sum = 0
    for y in range(1, N - 1):
        max_sum = max(max_sum, left[y - 1] + right[y + 1])

    return max_sum
