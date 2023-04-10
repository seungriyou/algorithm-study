def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid

    elif arr[mid] > mid:
        return binary_search(arr, start, mid - 1)

    else:
        return binary_search(arr, mid + 1, end)

N = int(input())
nums = list(map(int, input().split()))

fixed_point = binary_search(nums, 0, N - 1)
if fixed_point:
    print(fixed_point)
else:
    print(-1)
