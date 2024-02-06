# https://www.acmicpc.net/problem/1654
import sys; input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

start = 1           # 0부터 시작하면 X
end = max(lans)
result = 0

def get_pieces(unit):
    return sum(lan // unit for lan in lans)

while start <= end:
    mid = (start + end) // 2

    if get_pieces(mid) < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
