# 로무토 파티션 방식 (항상 맨 오른쪽의 피벗을 택하는 단순한 방식)
# 파이썬 알고리즘 인터뷰 / https://modoocode.com/248

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]  # 가장 오른쪽을 피벗으로 설정

        # left, right는 가장 왼쪽에서 시작
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                # left와 right를 swap하고 둘 다 한 칸 이동
                A[left], A[right] = A[right], A[left]
                left += 1
            # else: right만 한 칸 이동

        # right가 끝에 도달하면 left와 pivot을 swap
        A[left], A[hi] = A[hi], A[left]

        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick_sort(A, lo, pivot - 1)
        quick_sort(A, pivot + 1, hi)

quick_sort(array, 0, len(array) - 1)
print(array)
