n, m = map(int, input().split())
# cards = []
# for _ in range(n):
#     cards.append(list(map(int, input().split())))
#
# print(max([min(row) for row in cards]))

result = 0
for _ in range(n):
    row = list(map(int, input().split()))
    min_card = min(row)
    result = max(min_card, result)

print(result)
