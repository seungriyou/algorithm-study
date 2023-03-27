n = int(input())
items = list(map(int, input().split()))
m = int(input())
requested_items = list(map(int, input().split()))

items.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for i in requested_items:
    if binary_search(items, i, 0, n - 1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
