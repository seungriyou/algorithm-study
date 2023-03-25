n = int(input())
data = []

for _ in range(n):
    data.append(input().split())

data.sort(key=lambda x: int(x[1]))

for d in data:
    print(d[0], end=" ")
