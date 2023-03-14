def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    # 찾은 경우, 중간점 인덱스 반환
    if array[mid] == target:
        return mid

    # 중간점의 값 > 찾고자 하는 값: 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    # 중간점의 값 < 찾고자 하는 값: 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)
