n, m = map(int, input().split())
ddeok = list(map(int, input().split()))
ddeok.sort()

start = 0
end = max(ddeok)

while (start <= end):
    mid = (start + end) // 2
    total = 0
    for d in ddeok:
        if d - mid > 0:
            total += (d - mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
