# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    from collections import deque

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(room, x, y):
        q = deque([(x, y, 0)])  # (x 좌표, y 좌표, 거리)
        visited = {(x, y)}

        while q:
            x, y, c = q.popleft()

            # 맨해튼 거리 2 이내에서만 확인
            if c >= 2:
                break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visited:
                    # 빈 테이블이라면 거리 세기
                    if room[nx][ny] == "O":
                        q.append((nx, ny, c + 1))
                        visited.add((nx, ny))
                    # P라면 거리두기가 조건에 맞게 지켜지지 않는 상황이므로 빠르게 False 반환
                    elif room[nx][ny] == "P":
                        return False

        # 거리두기가 조건에 맞게 잘 지켜지고 있으므로 True 반환
        return True

    def check(room):
        """해당 대기실에서 모든 응시자가 거리두기를 지키고 있는지 여부를 1/0으로 반환하는 함수"""

        # P의 좌표를 set으로 모으기
        p_pos = {(i, j) for i in range(5) for j in range(5) if room[i][j] == "P"}

        # P의 좌표마다 bfs 돌면서, 조건에 맞게 거리두기가 지켜지지 않는 경우가 발생하는지 확인
        # 지켜지지 않는 경우가 있다면 빠르게 0 반환
        for x, y in p_pos:
            if not bfs(room, x, y):
                return 0

        # 모든 P의 좌표에 대해 거리두기가 잘 지켜짐을 확인했다면 1 반환
        return 1

    return [check(room) for room in places]
