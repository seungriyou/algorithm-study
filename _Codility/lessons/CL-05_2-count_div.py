# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

# 첫 번째 풀이: https://app.codility.com/demo/results/trainingA4N72S-TU8/
# prefix sum을 이용하지 않았다.. x_x
def solution(A, B, K):
    a = A + (K - A % K if A % K else 0)
    b = B - (B % K)

    return (b - a) // K + 1


# 두 번째 풀이: https://app.codility.com/demo/results/training2YN3AA-TKY/
# prefix sum 아이디어를 이용했다.
def solution(A, B, K):
    if A == 0:
        # 0 mod K도 0이므로, 0도 세어준다.
        return B // K + 1
    else:
        # (B 까지의 K 배수 개수) - (A - 1까지의 K 배수 개수)
        return B // K - (A - 1) // K
