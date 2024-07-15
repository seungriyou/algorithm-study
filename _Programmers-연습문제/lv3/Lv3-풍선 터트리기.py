# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    answer = 0

    n = len(a)
    if n <= 2:
        return n

    # min_left[i] = a[i]의 왼쪽 원소 중 최솟값
    # min_right[i] = a[i]의 오른쪽 원소 중 최솟값
    min_left = a[:]
    min_right = a[:]

    for i in range(1, n):
        min_left[i] = min(a[i - 1], min_left[i - 1])

    for i in range(n - 2, -1, -1):
        min_right[i] = min(a[i + 1], min_right[i + 1])

    # a[i]가 min_left[i] 값과 min_right[i] 값보다 크다면, 터트릴 수밖에 없음 (**여집합을 생각해야 했다..!)
    for i in range(n):
        if min_left[i] < a[i] and a[i] > min_right[i]:
            answer += 1

    # 전체 개수에서 터트릴 수밖에 없는 개수 빼기
    return n - answer
