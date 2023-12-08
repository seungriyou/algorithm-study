# https://www.acmicpc.net/problem/11000
import sys
import heapq
input = sys.stdin.readline

N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]

classes.sort()      # (s, t) 튜플들을 s 순으로 오름차순, s 값이 같을 경우 t 순으로 오름차순 정렬

q = []      # t를 기록하는 우선순위 큐 (기록된 t 중 가장 작은 값을 꺼내기 위함)
for i in range(N):
    s, t = classes[i]
    # 현재 보고있는 t를 우선순위 큐에 추가
    heapq.heappush(q, t)
    # 만약, 기록된 t 중 가장 작은 값이 현재 보고 있는 s보다 작거나 같은 값이라면 pop
    # (해당 강의실에서 현재 보고있는 수업까지 가능하므로)
    if q[0] <= s:
        heapq.heappop(q)
    # TIP: heapq 우선순위 큐의 경우, heapify 과정에서 매번 새로운 최소값이 [0] 인덱스에 위치되므로
    #      [0] 인덱스로 접근하여 최소값을 삭제하지 않고 얻을 수 있다!

# 우선순위 큐에 남아있는 t의 개수 == 필요한 강의실의 최소 개수
print(len(q))
