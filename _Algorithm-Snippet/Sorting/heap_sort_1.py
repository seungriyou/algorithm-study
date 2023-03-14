# 정석 구현
# https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    n = len(unsorted)

    # 1. 주어진 원소들로 최대 힙을 구성한다.
    for i in range(n // 2 - 1, -1, -1): # 인덱스: (n // 2 - 1) ~ 0
        # 최초 힙 구성 시 배열의 중간부터 시작하면
        # 이진 트리 성질에 의해 모든 요소 값을 서로 한 번씩 비교할 수 있다. -> O(n)
        heapify(unsorted, i, n)

    # 2. 원소의 개수만큼 다음을 반복 수행한다.
    # 한 번 힙이 구성되면 개별 노드는 최악의 경우에도 트리의 높이(logn) 만큼의 자리이동을 하게 된다.
    # 이러한 노드들이 n개 있으므로 -> O(nlogn)
    for i in range(n - 1, 0, -1):
        # 2-1. 최대 힙의 루트노드(= 첫번째 요소, 최댓값)와 말단노드(= 마지막 요소)를 교환한다.
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        # 2-2. 새로운 루트노드에 대해 최대 힙을 구성한다.
        # 즉, 최댓값이 뒤에서부터 차례로 쌓여가도록 한다.
        heapify(unsorted, 0, i)

    return unsorted

print(heap_sort(array))
