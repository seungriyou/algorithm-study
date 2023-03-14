# https://zetawiki.com/wiki/Python_%EC%89%98%EC%A0%95%EB%A0%AC_%EA%B5%AC%ED%98%84

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        # i = 각 부분 리스트의 두 번째 원소부터 시작하여,
				# 부분 리스트를 번갈아가며 점차 오른쪽으로 이동
        for i in range(gap, size):
            tmp = arr[i]
            j = i
            # j = i부터 점차 gap 만큼 왼쪽으로 이동하며 비교
            while j >= gap and arr[j - gap] > tmp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = tmp
        gap //= 2

    return arr

print(shell_sort(array))
