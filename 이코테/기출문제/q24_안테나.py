n = int(input())
house = list(map(int, input().split()))

"""distance = [sum(map(lambda x: abs(x - loc), house)) for loc in house]

print(sorted(list(zip(house, distance)), key=lambda x: (x[1], x[0]))[0][0])"""

# 그냥 정렬 후 중간값 출력하면 됨
house.sort()
print(house[(n - 1) // 2])
