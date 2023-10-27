# [PG] 43105 - 정수 삼각형 (Lv3)
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    for i in range(1, len(triangle)):   # -- height 만큼 반복
        for j in range(i + 1):   # -- i + 1 == 해당 level에서의 width
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:
                triangle[i][j] += triangle[i - 1][-1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    return max(triangle[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
assert 30 == solution(triangle)
