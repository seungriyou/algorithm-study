# heapq 모듈 사용
# https://www.daleseo.com/python-heapq/

from heapq import heappush, heappop

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def heap_sort(nums):
    heap = []
    for num in nums:
        heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heappop(heap))

    return sorted_nums

print(heap_sort(array))
