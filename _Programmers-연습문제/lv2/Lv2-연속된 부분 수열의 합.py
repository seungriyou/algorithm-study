# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = None
    right = sub_sum = 0
    n = len(sequence)
    min_len = n + 1

    for left in range(n):
        while right < n and sub_sum < k:
            sub_sum += sequence[right]
            right += 1

        if sub_sum == k and (new_len := right - left) < min_len:
            min_len = new_len
            answer = [left, right - 1]

        sub_sum -= sequence[left]

    return answer
