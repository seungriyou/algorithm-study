"""작은 순서대로 합쳐나갈 때 최소 횟수로 비교하게 됨"""
import heapq

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

result = 0

# heap 내 원소가 하나 남을 때까지 반복
while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    # 합쳐서 다시 heap에 삽입
    sum_val = first + second
    result += sum_val
    heapq.heappush(heap, sum_val)

print(result)
