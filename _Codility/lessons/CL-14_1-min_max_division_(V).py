# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/

# 첫 번째 풀이: https://app.codility.com/demo/results/trainingD3Y9D5-8FF/
def solution(K, M, A):
    start = max(A)  # lower bound
    end = sum(A)  # upper bound

    while start < end:
        mid = (start + end) // 2  # maximal sum of a block의 candidate
        # print(f"{start=} {end=}")

        if can_divide_more(A, mid, K):
            end = mid  # block의 maximal sum의 크기를 줄여서 block 수를 증가시키도록 함
        else:
            start = mid + 1  # block의 maximal sum의 크기를 늘려서 block 수를 감소시키도록 함

    return start


def can_divide_more(A, max_sum, max_num):
    block_cnt = temp_sum = 0

    for a in A:
        if temp_sum + a > max_sum:
            block_cnt += 1
            temp_sum = a
        else:
            temp_sum += a
    # print(f"... {max_sum=} {block_cnt=}")
    return block_cnt < max_num


# 두 번째 풀이(better): https://app.codility.com/demo/results/trainingEZW4E2-WXD/
# 실수하지 않게 번거롭더라도 더 명확하게 나타내자. (result 변수)
def solution(K, M, A):
    """
    binary search를 통해
    - 나누어진 block의 개수가 K가 되도록할 때
    - block의 maximal sum의 최솟값
    을 구한다.
    """

    # block의 maximal sum에 대한 lower bound, upper bound
    start = max(A)  # lower bound (block에 A에서 가장 큰 값 단 하나만 들어가는 경우)
    end = sum(A)  # upper bound
    result = end

    while start <= end:
        mid = (start + end) // 2  # 확인해볼 maximal sum candidate
        # print(f"{start=} {end=} / {mid=}")

        # block을 더 많은 개수로 나눌 수 있다면, maximal sum의 값은 더 작아져야 한다.
        if is_divisible(A, mid, K):
            result = mid  # (divisible 할 때마다 maximal sum의 값은 작아질 것이므로) result에 기록
            end = mid - 1
            # print(f"{result=}")
        else:
            start = mid + 1

    return result


def is_divisible(A, max_sum, max_cnt):
    """
    주어진 block의 max_sum 제한에 따라 block을 나누었을 때
    나누어진 block의 개수가 max_cnt보다 작으면 더 나눌 수 있다.
    """
    cnt = tmp_sum = 0

    for a in A:
        if tmp_sum + a > max_sum:
            cnt += 1
            tmp_sum = a
        else:
            tmp_sum += a

    return cnt < max_cnt  # cnt가 max_cnt보다 작다면 더 많은 개수의 block으로 나눌 수 있다 (True)
