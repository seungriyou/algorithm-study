n, m = map(int, input().split())
current = []
for _ in range(n):
    current.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for c in current:
    for i in range(c, m + 1):
        if d[i - c] != 1001:
            d[i] = min(d[i], d[i - c] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
