# https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

bubble_sort(array)
print(array)
