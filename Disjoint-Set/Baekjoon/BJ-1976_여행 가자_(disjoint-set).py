# https://www.acmicpc.net/problem/1976
import sys; input = sys.stdin.readline

# BFS로도 풀 수 있다!

N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

parent = list(range(N + 1))

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            union_parent(i + 1, j + 1)

answer = "YES"
for i in range(1, M):
    # start 도시의 parent와 같은지 확인
    if parent[plan[i]] != parent[plan[0]]:
        answer = "NO"
        break
print(answer)
