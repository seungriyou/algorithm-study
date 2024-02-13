# https://www.acmicpc.net/problem/15686
import sys; input = sys.stdin.readline

N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]

# === 함수 === #
# 집의 치킨 거리를 구하는 함수
def get_house_chicken_distance(hr, hc, selected_chickens):
    chicken_distance = 2 * N

    for cr, cc in selected_chickens:
        chicken_distance = min(chicken_distance, abs(hr - cr) + abs(hc - cc))

    return chicken_distance

# 도시의 치킨 거리를 구하는 함수
def get_city_chicken_distance(selected_chickens):
    chicken_distance = 0

    for hr, hc in houses:
        chicken_distance += get_house_chicken_distance(hr, hc, selected_chickens)

    return chicken_distance

# 1. 치킨집과 집의 좌표 찾기
chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if cities[i][j] == 1:
            houses.append((i, j))
        elif cities[i][j] == 2:
            chickens.append((i, j))

n_chickens = len(chickens)
selected_chickens = set()
min_chicken_distance = int(1e9)

# 2. 백트래킹
def backtrack(idx):
    global min_chicken_distance

    # base condition
    if len(selected_chickens) == M:
        min_chicken_distance = min(min_chicken_distance, get_city_chicken_distance(selected_chickens))
        return

    # recur
    for i in range(idx, n_chickens):
        selected_chickens.add(chickens[i])
        backtrack(i + 1)
        selected_chickens.remove(chickens[i])


backtrack(0)

print(min_chicken_distance)
