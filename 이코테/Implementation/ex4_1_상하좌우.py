n = int(input())
plan = list(input().split())

d = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

x, y = 1, 1

for p in plan:
    nx = x + d[p][0]
    ny = y + d[p][1]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x, y = nx, ny

print(x, y)
