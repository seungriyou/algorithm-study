import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

import heapq
from collections import defaultdict

Q = int(input())


# TODO: 기억해야 할 것!
"""
1. 우선순위 -> heapq를 사용할 생각을 하자. 필요한 heapq가 무엇이고, 어느 시점에서 pop/push 해야하는가?
2. 항상 클래스가 답일까? 함수를 잘 짜자.
3. 입력 값 크기 보고, 1억번 이상 돌 것 같은 동작은 최적화해야 한다.
4. 하나를 제외한 전체를 바꾸기보다, 하나를 바꾸는 방법을 사용해야 최적화할 수 있다.
5. 줄일 수 있는 건 최대한 줄이자. (중복!!!)
"""

"""
- 격자: N*M
- 토끼: P마리
    - (pid, d) = (고유번호, 이동해야 하는 거리)
    - 첫 위치는 (0, 0)

[ 우선순위 ]
- 경주 진행 - K번 반복 시: 토끼
    - for_moving_rabbit: 내부에 계속 토끼 개수만큼 유지될 것 (초기화 때 생성하기)
        (총 점프 횟수, 행+열, 행, 열, 고유번호)
- 경주 진행 - K번 반복 시: 이동해야 할 위치
    - for_moving_loc
        (-(행+열), -행, -열)
- 경주 진행 - K번 반복 이후: 토끼
    - for_score
        (-(행+열), -행, -열, -고유번호)
        defaultdict로 K번 반복 때마다 갱신되도록 관리하기
        

[ 경주 진행 : 200 ] (K, S)
=> 가장 우선순위가 높은 토끼를 뽑아 멀리 보내주는 것을 K번 반복

1. K번 반복
    - 우선순위 높은 토끼 뽑기
        - (현재까지의 총 점프 횟수가 적은 토끼, 
            현재 서있는 행 번호 + 열 번호가 작은 토끼, 
            행 번호가 작은 토끼, 
            열 번호가 작은 토끼, 
            고유번호가 작은 토끼)
    - 우선순위 가장 높은 토끼 이동 & 나머지 토끼 점수 얻기
        - 우선순위 가장 높은 토끼가 i번일 때, 상하좌우 네 방향으로 각각 di 만큼 이동했을 때의 위치 구하기
        - 도중에, 다음 칸이 격자를 벗어나게 되면 방향을 반대로 바꿔 한 칸 이동
        - 구해진 4개 위치 중 (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 순으로 우선순위 가장 높은 칸 골라서 토끼 이동
        - 이동한 위치를 (r, c)라 했을 때 i번 토끼 제외한 나머지 P - 1마리 토끼들은 모두 r + c 만큼의 점수를 동시에 얻음
2. 이후
    - K번 턴 동안 한 번이라도 뽑혔던 적 있는 토끼 중, 우선순위 가장 높은 토끼 골라 점수 S 더해주기
        - 우선순위: (현재 서있는 행 번호 + 열 번호가 큰 토끼, 행 번호가 큰 토끼, 열 번호가 큰 토끼, 고유번호가 큰 토끼) 순
    

[ 이동거리 변경 : 300 ] (pid_t, L)
고유번호 pid_t인 토끼의 이동거리를 L배 해줌


[ 최고의 토끼 선정 : 400 ]
- 각 토끼가 모든 경주를 진행하며 얻은 점수 중 가장 높은 점수 출력

"""

# 상우하좌
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

# 점수
score = 0

def can_go(r, c):
    return 0 <= r < N and 0 <= c < M

def out_of_range(r, c):
    # TODO: ?!!
    r %= 2 * (N - 1)
    c %= 2 * (M - 1)

    return min(r, 2 * (N - 1) - r), min(c, 2 * (M - 1) - c)

class Rabbit:
    def __init__(self, pid, d):
        self.pid = pid
        self.d = d
        self.loc = (0, 0)   # 초기 위치
        self.score = 0      # 초기 점수
        self.count = 0      # 총 점프 횟수

    def __repr__(self):
        return f"<Rabbit #{self.pid}> d={self.d} loc={self.loc} score={self.score} count={self.count}"

    def move(self):
        """
        - 상하좌우 네 방향으로 각각 d 만큼 이동했을 때의 위치 구하기
        - 도중에, 다음 칸이 격자를 벗어나게 되면 방향을 반대로 바꿔 한 칸 이동
        - 구해진 4개 위치 중 (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 순으로 우선순위 가장 높은 칸 골라서 토끼 이동
        - 업데이트: count, loc
        """
        # 상하좌우 네 방향에 대해, (-(행+열), -행, -열) 모으기
        for_moving_loc = []

        r, c = self.loc
        for i in range(4):
            nr, nc = r + dr[i] * self.d, c + dc[i] * self.d

            # 격자를 벗어나면 다시 구하기
            if not can_go(nr, nc):
                nr, nc = out_of_range(nr, nc)

            heapq.heappush(for_moving_loc, (-(nr + nc), -nr, -nc))

        # 내림차순 정렬 후 [0]의 위치로 이동
        nrnc, nr, nc = heapq.heappop(for_moving_loc)
        self.loc = (-nr, -nc)

        # count 값 증가
        self.count += 1

        return self.count, nrnc, nr, nc     # (총 점프 횟수, -(행+열), -행, -열)

    def add_score(self, score):
        self.score += score

    def change_dist(self, L):
        self.d *= L

##########
def race(K, S):
    """
    1. K번 반복
        - 우선순위 높은 토끼 뽑기
            - (현재까지의 총 점프 횟수가 적은 토끼, 
                현재 서있는 행 번호 + 열 번호가 작은 토끼, 
                행 번호가 작은 토끼, 
                열 번호가 작은 토끼, 
                고유번호가 작은 토끼)
        - 우선순위 가장 높은 토끼 이동 & 나머지 토끼 점수 얻기
            - 우선순위 가장 높은 토끼가 i번일 때, 상하좌우 네 방향으로 각각 di 만큼 이동했을 때의 위치 구하기
            - 도중에, 다음 칸이 격자를 벗어나게 되면 방향을 반대로 바꿔 한 칸 이동
            - 구해진 4개 위치 중 (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 순으로 우선순위 가장 높은 칸 골라서 토끼 이동
            - 이동한 위치를 (r, c)라 했을 때 i번 토끼 제외한 나머지 P - 1마리 토끼들은 모두 r + c 만큼의 점수를 동시에 얻음
    2. 이후
        - K번 턴 동안 한 번이라도 뽑혔던 적 있는 토끼 중, 우선순위 가장 높은 토끼 골라 점수 S 더해주기
            - 우선순위: (현재 서있는 행 번호 + 열 번호가 큰 토끼, 행 번호가 큰 토끼, 열 번호가 큰 토끼, 고유번호가 큰 토끼) 순
    """
    global score

    selected_rabbits = defaultdict(tuple)   # (-(행+열), -행, -열, -고유번호)

    # 1. K번 반복
    for _ in range(K):
        # 우선순위 높은 토끼 뽑기 (총 점프 횟수, 행+열, 행, 열, 고유번호)
        _, rc, r, c, pid = heapq.heappop(for_moving_rabbit)
        picked_rabbit = rabbits[pid]

        # 우선순위 높은 토끼 이동 (총 점프 횟수, -(행+열), -행, -열)
        cnt, rc, r, c = picked_rabbit.move()

        # 우선순위 높은 토끼 selected_rabbits 기록 (-(행+열), -행, -열, -고유번호)
        selected_rabbits[pid] = (rc, r, c, -pid)

        # 나머지 토끼 점수 얻기:
        # (1) global score에 점수를 더하고
        score += -rc + 2
        # (2) 선택된 토끼의 점수를 빼기
        picked_rabbit.score -= -rc + 2

        # 다시 for_moving_rabbit에 넣어주기
        heapq.heappush(for_moving_rabbit, (cnt, -rc, -r, -c, pid))

    # 2. 이후
    # _min = (1, 1, 1, 1)
    # for sr in selected_rabbits.values():
    #     _min = min(_min, sr)
    # rabbits[-_min[3]].add_score(S)
    _, _, _, pid = sorted(selected_rabbits.values())[0]
    rabbits[-pid].add_score(S)

def change_distance(pid_t, L):
    """
    고유번호 pid_t인 토끼의 이동거리를 L배 해줌
    """
    rabbits[pid_t].change_dist(L)

def pick_best_rabbit_score():
    max_score = -float('inf')
    for rabbit in rabbits.values():
        max_score = max(max_score, rabbit.score)
    return max_score + score

##########
def print_rabbits():
    for pid, rabbit in rabbits.items():
        print(rabbit)

if __name__ == "__main__":
    # 이동할 토끼를 고르기 위한 heapq
    for_moving_rabbit = []

    # 100으로 시작하는 첫 command -> 초기화
    _, N, M, P, *_rabbits = map(int, input().split())

    # rabbits dictionary 생성
    rabbits = dict()
    for i in range(P):
        pid, d = _rabbits[2 * i], _rabbits[2 * i + 1]
        rabbits[pid] = Rabbit(pid, d)

        # 이동할 토끼를 고르기 위한 heapq에 담기: (총 점프 횟수, 행+열, 행, 열, 고유번호)
        heapq.heappush(for_moving_rabbit, (0, 0, 0, 0, pid))

    for _ in range(Q - 1):
        cmd, *param = tuple(map(int, input().split()))

        if cmd == 200:
            print("200")
            race(*param)

        elif cmd == 300:
            print("300")
            change_distance(*param)
            print_rabbits()

        elif cmd == 400:
            print_rabbits()
            print(pick_best_rabbit_score())
