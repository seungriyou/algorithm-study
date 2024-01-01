# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

# 첫 번째 풀이 (77%): https://app.codility.com/demo/results/trainingG2WYYC-FUU/
def solution(N, A):
    counter = [0] * N
    max_val = 0

    for a in A:
        # a == N + 1: max counter
        if a == N + 1:
            counter = [max_val] * N

        # a <= N: increase by 1
        else:
            counter[a - 1] += 1
            max_val = max(max_val, counter[a - 1])

    return counter


# 두 번째 풀이 (100%, O(N+M)): https://app.codility.com/demo/results/trainingUC8H5N-RVE/
# 각 연산에서마다 max counter 연산을 곧바로 수행하지 않는 것이 관건이다! (이렇게 하면 O(N^2)이 되므로)
def solution(N, A):
    # max counter 연산을 그때 그때 수행하면 performance 100% 나오지 않음
    counter = [0] * N
    prev_max_val = max_val = 0

    # 연산 차례대로 수행
    for a in A:
        if a > N:
            # max counter 연산을 곧바로 수행하는 것이 아닌,
            # prev_max_val(= max counter 연산의 기준값)에 현재의 max_val 저장
            prev_max_val = max_val

        else:
            # prev_max_val에 저장되어 있던 값과 비교하여 최댓값을 저장
            counter[a - 1] = max(counter[a - 1], prev_max_val)
            # counter increase
            counter[a - 1] += 1
            # 현재 증가시킨 counter 값 기반으로 max_val 업데이트
            max_val = max(max_val, counter[a - 1])

    # 마지막으로 prev_max_val보다 작은 원소는 prev_max_val로 변경
    return [max(c, prev_max_val) for c in counter]
