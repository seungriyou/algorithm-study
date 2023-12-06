# https://www.acmicpc.net/problem/11728
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []
p1 = p2 = 0
while p1 < n and p2 < m:
    if arr1[p1] < arr2[p2]:
        result.append(arr1[p1])
        p1 += 1
    else:
        result.append(arr2[p2])
        p2 += 1

# result += arr1[p1:]
# result += arr2[p2:]
for i in range(p1, n):
    result.append(arr1[i])
for i in range(p2, m):
    result.append(arr2[i])

print(*result)
