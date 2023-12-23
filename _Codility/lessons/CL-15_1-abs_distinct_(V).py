# https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct/

# [sol1] https://app.codility.com/demo/results/training675VV2-C6W/ (중복된 로직이 많고 깔끔하지 않은 풀이)
def solution(A):
    left, right = 0, len(A) - 1
    cnt = 0

    # A에 음수와 양수가 모두 존재하는 경우
    while A[left] < 0 and A[right] > 0:
        while left < len(A) - 1 and A[left] == A[left + 1]:
            left += 1
        while right > 0 and A[right] == A[right - 1]:
            right -= 1

        if -A[left] < A[right]:
            cnt += 1
            right -= 1
        elif -A[left] > A[right]:
            cnt += 1
            left += 1
        else:
            cnt += 1
            right -= 1
            left += 1

    # A가 모두 <= 0이거나 >= 0인 경우 (+ 위의 while문의 실행 결과 이어서 진행)
    while left <= right:
        while left < len(A) - 1 and A[left] == A[left + 1]:
            left += 1
        cnt += 1
        left += 1

    return cnt


# [sol2] https://app.codility.com/demo/results/trainingGQVSRM-MJK/ (참고)
def solution(A):
    left, right = 0, len(A) - 1
    cnt = 0

    while left <= right:
        cnt += 1
        mval = max(abs(A[left]), abs(A[right]))

        while left <= right and abs(A[left]) == mval:
            left += 1
        while left <= right and abs(A[right]) == mval:
            right -= 1

    return cnt
