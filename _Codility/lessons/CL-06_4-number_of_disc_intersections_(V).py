# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
# https://app.codility.com/demo/results/trainingXUMN7K-FDT/

def solution(A):
    # ref: https://darkstart.tistory.com/195

    # disc와 x축의 두 교점 left와 right를 모은다. (radius: 반지름)
    left = []
    right = []
    for i, a in enumerate(A):
        left.append(i - a)
        right.append(i + a)

    # left와 right를 각각 오름차순 정렬한다.
    left.sort()
    right.sort()

    # right[i] >= left[j]이면 두 disc가 intersect 한다.
    j = 0
    cnt = 0
    for i in range(len(A)):
        while j < len(A) and right[i] >= left[j]:
            cnt += j
            cnt -= i  # 중복 계산 및 더이상 겹치지 않는 원의 계산을 방지한다.
            j += 1

    # cnt > 10_000_000 이면 -1을 반환한다.
    return -1 if cnt > 10_000_000 else cnt
