start = input()
col = ord(start[0]) - ord('a') + 1
row = int(start[1])

cases = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
cnt = 0

for case in cases:
    ncol = col + case[0]
    nrow = row + case[1]
    if ncol >= 1 and ncol <= 8 and nrow >= 1 and nrow <= 8:
        cnt += 1

print(cnt)
