# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
# https://app.codility.com/demo/results/training9DXCH8-8GU/

def solution(A):
    """
    * A가 오름차순 정렬되어 있다고 가정한다.
    * [...]: maximal product를 가지는 triplet
    (1) 모두 양수(+ 0)인 경우
        1, 2, 3, 4, 5, [6, 7, 8]
    (2) 모두 음수(+ 0)인 경우
        -6, -5, -4, -3, [-2, -1, 0]
    (3) 양수와 음수가 모두 존재하는 경우
        -5, -4], -3, 0, [3
    => A[-1]는 무조건 triplet에 포함되어야 한다!
    """
    A.sort()
    # 오름차순 정렬 후, 다음 두 값 중에 maximal product of any triplet 존재
    return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
