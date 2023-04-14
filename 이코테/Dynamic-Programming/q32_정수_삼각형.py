import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    depth = len(triangle[i])
    for j in range(depth):
        if j == 0:
            upper_left = 0
        else:
            upper_left = triangle[i - 1][j - 1]
        if j == depth - 1:
            upper_right = 0
        else:
            upper_right = triangle[i - 1][j]

        triangle[i][j] += max(upper_left, upper_right)

print(max(triangle[n - 1]))
