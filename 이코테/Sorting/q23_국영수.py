n = int(input())
students = []
for _ in range(n):
    data = input().split()
    students.append((data[0], *map(int, data[1:])))

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
    print(s[0])
