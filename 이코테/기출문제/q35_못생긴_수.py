n = int(input())

ugly = [0] * n
ugly[0] = 1 # 첫 번째 못 생긴 수는 1

# 작은 수부터 차례로 곱해나가면 됨
i2 = i3 = i5 = 0 # 2, 3, 5배를 위한 인덱스
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
    # elif로 하면 안 됨!
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n - 1])
