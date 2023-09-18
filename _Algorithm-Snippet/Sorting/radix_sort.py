# https://roytravel.tistory.com/328

from collections import deque

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def radix_sort(arr):
    buckets = [deque() for _ in range(10)]
    MAX = max(arr) # 가장 큰 자릿수를 알기 위함
    queue = deque(arr)
    radix = 1 # 1의 자리부터 시작

    # 가장 큰 수의 자릿수까지 반복
    while MAX >= radix:
        # 1. queue에 있는 데이터를 각 자릿수에 해당하는 bucket에 담는다.
        while queue:
            num = queue.popleft()
            buckets[(num // radix) % 10].append(num)
        # 2. bucket에 담은 데이터를 다시 차례로 queue에 담는다.
        for bucket in buckets:
            queue.append(bucket.popleft())

        # 자릿수를 늘려준다.
        radix *= 10

    return list(queue)

print(radix_sort(array))
