# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

# O(N^2) (60%): https://app.codility.com/demo/results/trainingPX2FTY-PFU/
def solution(A):
    # init
    min_avg = 10_001
    result = -1
    N = len(A)

    # prefix sum
    prefix_sum = [0] + A[:]
    for i in range(1, N + 1):
        prefix_sum[i] += prefix_sum[i - 1]

    for p in range(N):
        for q in range(p + 1, N):
            avg = (prefix_sum[q + 1] - prefix_sum[p]) / (q - p + 1)
            if avg < min_avg:
                min_avg = avg
                result = p

    return result


# O(N) (100%): https://app.codility.com/demo/results/trainingAKBE89-RH8/
def solution(A):
    """
    원소가 4개인 slice [a, b, c, d]에 대해,
    avg([a, b]) <= avg([c, d])라면 avg([a, b]) <= avg([a, b, c, d])가 된다.
    => 원소가 4개인 slice의 avg 값은, 원소가 2개인 slices로 나누었을 때의 각 avg 값 중 작은 값보다 작아질 수 없다.

    따라서
    - 초기 값을 맨 앞의 두 원소로 이루어진 slice의 avg 값으로 설정하고,
    - slice의 원소의 개수가 2, 3개(= 확인해야 할 최소 단위)인 slice의 avg 값을 순회하며 탐색한다.
    - 원소가 3개인 경우는 1개 + 2개인 경우로 나눌 수 있는데, 문제 조건에 따라서 1개인 경우는 없다. 따라서 원소의 개수 2, 3개인 slice만 확인한다.
    """

    # init: 맨 앞의 두 원소
    min_avg = (A[0] + A[1]) / 2
    min_idx = 0

    # 순회
    for i in range(2, len(A)):
        # 원소의 개수가 3인 경우
        avg = (A[i - 2] + A[i - 1] + A[i]) / 3
        if avg < min_avg:
            min_avg = avg
            min_idx = i - 2

        # 원소의 개수가 2인 경우
        avg = (A[i - 1] + A[i]) / 2
        if avg < min_avg:
            min_avg = avg
            min_idx = i - 1

    return min_idx
