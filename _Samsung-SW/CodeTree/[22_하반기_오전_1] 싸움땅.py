# https://www.codetree.ai/training-field/frequent-problems/problems/battle-ground
"""
- n: 격자 크기
- m: 플레이어의 수
- k: 라운드의 수

- 격자
    - 0: 빈칸
    - > 0: 총의 공격력

    - 무기가 있을 수 있음
    - 무기가 없는 빈 격자에 플레이어가 위치

    - 빨간색 숫자: 총의 경우 공격력, 플레이어의 경우 초기 능력치
    - 노란색 숫자: 플레이어 번호

- 플레이어
    - (x, y): 위치
    - d: 방향 (0, 1, 2, 3 = ↑, →, ↓, ←)
    - s: 초기 능력치 (모두 다름)
    - idx: 플레이어의 번호 (0 ~ n - 1)
    - point: 포인트
    - gun: 가지고 있는 총의 공격력

[ 라운드 ]
다음을 1 ~ n번 플레이어까지 순차적으로 진행:
1. 첫 번째 플레이어부터 순차적으로 방향대로 한 칸 이동
    - 격자를 벗어나는 경우, 정반대 방향으로 방향을 바꾸어서 1만큼 이동
2-(1). 이동한 곳에 플레이어가 없다면,
    - 총이 있는 경우:
        - 총을 가지지 않은 경우: 총 획득
        - 이미 총을 가진 경우: 놓여있는 총들과 플레이어가 가지고 있는 총 가운데 공격력이 더 쎈 총 획득, 나머지 총은 두기
2-(2). 이동한 곳에 플레이어가 있다면, 두 플레이어가 싸움
    - 점수 = (해당 플레이어의 초기 능력치) + (가지고 있는 총의 공격력)
    - 점수가 더 큰 플레이어가 이김, 같다면 초기 능력치가 높은 플레이어가 이김
        - 이긴 플레이어는 점수의 차이만큼 포인트로 획득

    - 진 플레이어:
        1. 가지고 있던 총을 해당 격자에 내려놓기
        2. 자신의 방향대로 한 칸 이동 (다른 플레이어가 있거나, 격자 벗어나는 경우, 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동)
        3. 해당 칸에 총이 있다면, 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려놓기
    - 이긴 플레이어:
        1. 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총 획득
        2. 나머지 총은 격자에 내려놓기

[ 총 ]
격자에, 각 cell 마다 최대힙으로 가지고 있기
-> 가장 공격력이 큰 총을 pop 및 [-1]로 조회할 수 있음

[ 플레이어 ]
> 가져야 할 값:
    - (x, y): 위치
    - d: 방향 (0, 1, 2, 3 = ↑, →, ↓, ←)
    - s: 초기 능력치 (모두 다름)
    - idx: 플레이어의 번호 (0 ~ n - 1)
    - point: 포인트
    - gun: 가지고 있는 총의 공격력

> 필요한 동작:
    - move(): 이동
        - 한 칸 이동 & 방향 전환 필요하다면 전환
    - 이동한 곳에 플레이어가 없을 때 (총 획득)
    - 이동한 곳에 플레이어가 있을 때 (싸우기)
    - get_score(): 초기 능력치 + 가지고 있는 총의 공격력 반환
    - earn_point(points): 이긴 경우, 포인트 벌기
    - lose(): 졌을 때의 동작
    - win(): 이겼을 때의 동작
    - get_gun(): 총 획득
        - (내가 가진 + 격자에 있는 총) 중에서 공격력이 쎈 총을 얻고, 나머지는 격자에 내려두기

[ 함수 ]
- is_valid(r, c, d): 해당 방향으로 한 칸 이동했을 때, 격자를 벗어나는지 여부
    - input: 현재 좌표 r, c, 방향 d
    - output: boolean (true/false)
- get_player_idx(r, c): 해당 위치에 플레이어가 위치하는지, 그 idx는 몇인지 반환
    - input: 좌표 r, c
    - output: int (-1: 없음 / 0~n-1: 존재하는 플레이어의 idx)
- fight(p1_idx, p2_idx): 두 플레이어가 싸울 때, 누가 이기는지
    - input: p1_idx, p2_idx
    - output: winner_idx, loser_idx
    - 점수가 더 큰 플레이어가 이김, 같다면 초기 능력치가 높은 플레이어가 이김
    - 이긴 플레이어에게는 포인트 ++
    - 진 플레이어는 lose(), 이긴 플레이어는 win() 실행
"""
import heapq

# def debug(mat):
#     for row in mat:
#         print(row)
#     print()

n, m, k = map(int, input().split())
guns = [list(map(int, input().split())) for _ in range(n)]
for gun in guns:
    for i in range(n):
        if gun[i] == 0:
            gun[i] = []
        else:
            gun[i] = [-gun[i]]  # 최대힙 구성하기 위해 음수로 넣기

"""
[[1], [2], [], [1], [2]]
[[1], [], [3], [3], [1]]
[[1], [3], [], [2], [3]]
[[2], [1], [2], [4], [5]]
[[], [1], [3], [2], []]
"""

# (0, 1, 2, 3 = ↑, →, ↓, ←)
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def is_valid(r, c, d):
    nr, nc = r + dr[d], c + dc[d]
    if nr < 0 or nr >= n or nc < 0 or nc >= n:
        return False
    return True

def get_player_idx(r, c):
    for player in players:
        if r == player.r and c == player.c:
            return player.idx
    return -1

def fight(p1_idx, p2_idx):
    p1, p2 = players[p1_idx], players[p2_idx]

    # 점수가 더 큰 플레이어가 이김, 같다면 초기 능력치가 높은 플레이어가 이김
    if (p1_score := p1.get_score()) > (p2_score := p2.get_score()):
        winner, loser = p1, p2
    elif p1_score < p2_score:
        winner, loser = p2, p1
    else:
        if p1.s > p2.s:
            winner, loser = p1, p2
        else:
            winner, loser = p2, p1

    # 이긴 플레이어에게는 포인트++
    winner.earn_point(abs(p1_score - p2_score))

    # 진 플레이어는 lose(), 이긴 플레이어는 win() 실행
    loser.lose()
    winner.win()

def print_result(players):
    print(*[player.point for player in players])

class Player:
    def __init__(self, r, c, d, s, idx, point=0, gun=0):
        self.r = r
        self.c = c
        self.d = d
        self.s = s  # 초기 능력치 (모두 다름)
        self.idx = idx  # 플레이어의 번호 (0 ~ n - 1)
        self.point = point
        self.gun = gun  # 가지고 있는 총의 공격력 (0이면 총이 없는 것)

    def __repr__(self) -> str:
        return f"<Player #{self.idx}> r={self.r}, c={self.c}, d={self.d}, s={self.s} " \
               f"point={self.point}, gun={self.gun if self.gun else 'X'}"

    def get_next_pos(self) -> tuple[int, int]:
        """한 칸 이동 & 방향 전환 필요하다면 전환할 때의 이동할 위치 반환"""
        # 격자를 벗어나는 경우, 정반대 방향으로 방향을 바꾸어서 1만큼 이동
        if not is_valid(self.r, self.c, self.d):
            self.d = (self.d + 2) % 4
        return self.r + dr[self.d], self.c + dc[self.d]

    def move(self, r, c) -> None:
        """주어진 위치로 이동"""
        self.r, self.c = r, c

    def get_score(self) -> int:
        """초기 능력치 + 가지고 있는 총의 공격력 반환"""
        return self.s + self.gun

    def earn_point(self, points: int) -> None:
        """이긴 경우, 포인트 벌기"""
        self.point += points

    def lose(self) -> None:
        """
        졌을 때의 동작
        1. 가지고 있던 총을 해당 격자에 내려놓기
        2. 자신의 방향대로 한 칸 이동 (다른 플레이어가 있거나, 격자 벗어나는 경우, 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동)
        3. 해당 칸에 총이 있다면, 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려놓기
        """
        # 1. 가지고 있던 총을 해당 격자에 내려놓기
        if self.gun:
            heapq.heappush(guns[self.r][self.c], -self.gun)
            self.gun = 0

        # 2. 자신의 방향대로 한 칸 이동
        # 다른 플레이어가 있거나, 격자 벗어나는 경우, 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동
        for i in range(4):
            d = (self.d + i) % 4
            # 해당 위치가 격자 내고, 해당 위치에 아무도 없다면 이동 가능
            if is_valid(self.r, self.c, d) and get_player_idx(self.r + dr[d], self.c + dc[d]) == -1:
                self.r = self.r + dr[d]
                self.c = self.c + dc[d]
                self.d = d
                break

        # 3. 해당 칸에 총이 있다면, 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려놓기
        if guns[self.r][self.c]:
            self.get_gun()

    def win(self) -> None:
        """
        이겼을 때의 동작
        1. 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총 획득
        2. 나머지 총은 격자에 내려놓기
        """
        if guns[self.r][self.c]:
            self.get_gun()


    def get_gun(self) -> None:
        """(내가 가진 + 격자에 있는 총) 중에서 공격력이 쎈 총을 얻고, 나머지는 격자에 내려두기"""
        # guns[r][c]가 존재함이 자명한 상황
        _guns = guns[self.r][self.c]

        # 플레이어가 총을 가지지 않은 경우, guns[r][c]에서 제일 큰 것 얻기 (pop)
        if not self.gun:
            self.gun = -heapq.heappop(_guns)

        # 플레이어가 총을 가진 경우, 가진 것보다 guns[r][c][0]이 쎄다면 바꾸기
        # [주의] 우선순위 큐(heapq)에서 최솟값/최댓값을 구하려면 [0]을 봐야한다!!! 이런 어이없는 실수를...
        elif -_guns[0] > self.gun:
            heapq.heappush(_guns, -self.gun)
            self.gun = -heapq.heappop(_guns)


players = []
for i in range(m):
    r, c, d, s = map(int, input().split())
    players.append(Player(r=r - 1, c=c - 1, d=d, s=s, idx=i))


if __name__ == "__main__":
    for _ in range(k):
        for p1_idx, player in enumerate(players):
            # 1. 방향대로 한 칸 이동 가능한 위치 구하기
            r, c = player.get_next_pos()

            # 2. 이동한 곳에 플레이어 있는지 없는지에 따라 동작
            p2_idx = get_player_idx(r, c)   # 이동한 곳에 있는 플레이어 (없으면 -1)
            player.move(r, c)               # 현재 플레이어 이동
            # 2-1. 이동한 곳에 플레이어가 없다면 총 얻기
            if p2_idx == -1:
                if guns[r][c]:
                    player.get_gun()
            # 2-2. 이동한 곳에 플레이어가 있다면 싸우기
            else:
                fight(p1_idx, p2_idx)

    print_result(players)
