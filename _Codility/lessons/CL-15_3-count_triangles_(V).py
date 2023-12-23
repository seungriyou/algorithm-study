# https://app.codility.com/programmers/lessons/15-caterpillar_method/count_triangles/

# O(N^2) 풀이: 100%
# https://app.codility.com/demo/results/trainingG2AS7J-XV8/
def solution(A):
    # A를 오름차순 정렬한다.
    A.sort()
    cnt = 0

    for p in range(len(A)):
        """
        모든 q마다 r을 q + 1으로 당겨서 하나하나 확인하게 되면 O(N^3)가 된다.
        r은 q와 상관없이 계속 누적해나가면서, A[p] + A[q] > A[r]을 만족하는 A[r]의 최댓값을 찾는다고 생각하면 된다.
        이렇게 하면 모든 q마다 r을 q + 1부터 확인하는 수고를 덜 수 있다. (complexity도 O(N^2)으로 최적화 가능)
        이는 A를 오름차순으로 정렬하였으므로, q가 증가함에 따라 A[q]도 계속 증가하기 때문에 가능하다.
        * 모든 p에 대해 q와 r이 O(N)번 증가하므로 O(N^2)이다.
        """
        r = p + 2  # r은 p 기준으로만 초기화를 수행한다.
        for q in range(p + 1, len(A)):
            while r < len(A) and A[p] + A[q] > A[r]:  # 오름차순 정렬했으므로, 이 기준만 만족하면 다른 기준도 만족한다.
                r += 1
            cnt += r - q - 1  # 조건을 만족하는 r 값은 (r - 1) ~ (q + 1)이 될 것이므로, 그 개수인 (r - q - 1)을 누적해서 더한다.

    return cnt


# O(N^3) 풀이: 63%
# https://app.codility.com/demo/results/training7WCRW4-2DW/
def solution(A):
    A.sort()
    cnt = 0

    for p in range(len(A)):
        for q in range(p + 1, len(A)):
            r = q + 1   # q 마다 r 새로 초기화
            while r < len(A) and A[p] + A[q] > A[r]:
                r += 1
            cnt += r - q - 1

    return cnt
