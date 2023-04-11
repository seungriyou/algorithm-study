"""input
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""

T = int(input())
test_case = []
for _ in range(T):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))
    mine_map = [golds[i - m:i] for i in range(m, len(golds) + 1, m)]
    test_case.append(mine_map)

for mine_map in test_case:
    n = len(mine_map)
    m = len(mine_map[0])

    for j in range(1, m):
        for i in range(n):
            # upper_left
            if i == 0:
                upper_left = 0
            else:
                upper_left = mine_map[i - 1][j - 1]
            # lower_left
            if i == n - 1:
                lower_left = 0
            else:
                lower_left = mine_map[i + 1][j - 1]

            mine_map[i][j] += max(upper_left, mine_map[i][j-1], lower_left)

    max_gold = 0
    for row in mine_map:
        max_gold = max(max_gold, row[m - 1])

    print(max_gold)
