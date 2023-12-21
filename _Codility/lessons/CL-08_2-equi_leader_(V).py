# https://app.codility.com/programmers/lessons/8-leader/equi_leader/
# https://app.codility.com/demo/results/training68KCFN-C9X/

def solution(A):
    from collections import defaultdict

    """
    equileader가 존재한다면, equileader의 값은 global leader의 값과 동일할 것이다.
    따라서 전체에서 global leader가 존재하지 않는다면, 빠르게 종료할 수 있다.
    1. 좌측에서 우측으로 partition을 이동시켜가면서, 다음의 항목을 업데이트 해나간다.
        (1) left, right 각 부분의 원소 counter
        (2) left, right 각 부분의 길이
    2. left, right 각 부분에 대해 모두 counter[leader] > len // 2 라면 equileader가 존재하는 경우이다.
    """

    # right 부분의 counter와 len의 초기값을 설정한다.
    right_counter = defaultdict(int)
    right_len = len(A)
    max_a = max_cnt = 0  # max_a는 global leader의 candidate이 된다.
    for a in A:
        right_counter[a] += 1
        if max_cnt < right_counter[a]:
            max_cnt = right_counter[a]
            max_a = a

    # max_a가 global leader가 맞는지 확인하고, 맞다면 max_a를 leader로 할당한다.
    # 각 부분에서 equileader가 존재한다면, 그 값은 global leader와 동일할 것이다.
    if max_cnt <= len(A) // 2:
        return 0
    leader = max_a

    # left 부분의 counter와 len의 초기값을 설정한다.
    left_counter = {a: 0 for a in A}
    left_len = 0

    # 좌측부터 우측으로 partition을 나눠가며 확인한다.
    equileader_cnt = 0
    for i in range(len(A) - 1):     # i = left 부분에 새로 포함될 원소의 index
        # left, right 각 부분 업데이트
        left_counter[A[i]] += 1
        left_len += 1
        right_counter[A[i]] -= 1
        right_len -= 1

        # equileader인 상황이라면 cnt++
        if left_counter[leader] > left_len // 2 and right_counter[leader] > right_len // 2:
            equileader_cnt += 1

    return equileader_cnt
