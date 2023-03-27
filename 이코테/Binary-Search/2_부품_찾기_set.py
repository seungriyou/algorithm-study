n = int(input())
items = set(map(int, input().split()))
m = int(input())
requested_items = list(map(int, input().split()))

for i in requested_items:
    if i in items:
        print("yes", end=" ")
    else:
        print("no", end=" ")
