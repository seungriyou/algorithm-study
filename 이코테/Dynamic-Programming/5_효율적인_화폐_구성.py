n, m = map(int, input().split())
current = []
for _ in range(n):
    current.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

# current가 정렬될 필요가 있나?

for c in current:
    for i in range(c, m + 1):
        if d[i - c] != 10001: # (i - c)원을 만드는 방법이 존재하는 경우 (해당 조건 없어도 됨)
            d[i] = min(d[i], d[i - c] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
