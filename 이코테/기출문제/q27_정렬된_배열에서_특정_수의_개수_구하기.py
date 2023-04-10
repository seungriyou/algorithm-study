from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
nums = list(map(int, input().split()))

def count_by_range(arr, left_val, right_val):
    right_idx = bisect_right(arr, right_val)
    left_idx = bisect_left(arr, left_val)
    return right_idx - left_idx

cnt = count_by_range(nums, x, x)
if cnt == 0:
    print(-1)
else:
    print(cnt)

