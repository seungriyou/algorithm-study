n, m = map(int, input().split())
x, y, d = map(int, input().split())

game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1 # 시작 위치 방문 처리

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1 # 방문한 칸 수
turn_cnt = 0

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] or game_map[nx][ny] == 1:
        turn_cnt += 1
    else:
        visited[nx][ny] = 1
        x = nx
        y = ny
        turn_cnt = 0
        cnt += 1

    if turn_cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
            turn_cnt = 0
        else:
            break

print(cnt)
