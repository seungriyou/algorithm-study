# [BJ] 2805 - 나무 자르기
# https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0           # 최소 값
end = max(trees)    # 최대 값

while start <= end:
    mid = start + (end - start) // 2
    total = 0
    for tree in trees:
        if tree - mid > 0:
            total += (tree - mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
