x = int(input())

d = [0] * 30001
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1 # 1 빼기 연산을 했다고 가정 (항상 가능)
    # 2, 3, 5로 나누어 떨어질 때 조건에 따라서
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1) # 2로 나누기 연산
    elif i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1) # 3으로 나누기 연산
    elif i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1) # 5로 나누기 연산

print(d[x])
