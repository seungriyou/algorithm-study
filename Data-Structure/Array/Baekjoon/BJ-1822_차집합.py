# https://www.acmicpc.net/problem/1822
import sys
input = sys.stdin.readline

na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = list(map(int, input().split()))

for bi in b:
    if bi in a:
        a.remove(bi)

diff = list(a)
diff.sort()

print(len(diff))
for d in diff:
    print(d, end=" ")
