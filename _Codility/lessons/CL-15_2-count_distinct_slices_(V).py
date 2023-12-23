# https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/

# O(N) 풀이: 100%
# https://app.codility.com/demo/results/training7Z2HVK-JNQ/
def solution(M, A):
    cnt = 0
    start = 0
    next_start = [0] * (M + 1)  # next_start[i]: i가 다시 등장했을 때, 가능한 distinct slice의 start index

    # distinct slice의 양 끝 index를 (start, end)로 나타낸다고 가정한다.
    for end, a in enumerate(A):
        # start가 next_start[a]보다 작다면, start를 next_start[a]로 옮겨주어야 distinct slice를 만족한다.
        if start < next_start[a]:
            start = next_start[a]

        # 다음에 다시 a를 만나게 되면, 그 a를 end로 가지는 distinct slice의 start는 현재 end의 다음 값이 될 것이다.
        next_start[a] = end + 1

        cnt += end - start + 1

        if cnt > 1_000_000_000:
            return 1_000_000_000

    return cnt


# O(N*(N+M)) 풀이: 60%
# https://app.codility.com/demo/results/trainingFAHUF4-SRF/
# https://app.codility.com/demo/results/trainingCWSZGJ-S2W/
def solution(M, A):
    cnt = 0

    for left, a in enumerate(A):
        counter = [0] * (M + 1)  # non-negative integers & all elements in A <= M
        for right in range(left, len(A)):
            if counter[A[right]] > 0:
                break
            counter[A[right]] += 1
            cnt += 1

            if cnt > 1_000_000_000:
                return 1_000_000_000

    return cnt
