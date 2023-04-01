n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt = 0
result = 0

for d in data:
    cnt += 1
    if cnt >= d:
        cnt = 0
        result += 1

print(result)
