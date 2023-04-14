n = input()
mid = len(n) // 2
left = map(int, n[:mid])
right = map(int, n[mid:])

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
