# https://www.acmicpc.net/problem/2212
import sys; input = sys.stdin.readline

# BJ-13164와 비슷한 문제

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()  # 인접한 센서 간의 거리를 구하기 위해 오름차순 정렬

dist = [sensors[i] - sensors[i - 1] for i in range(1, N)]
dist.sort()     # 인접산 센서 간의 거리를 기준으로 오름차순 정렬

# 거리가 가장 긴 K - 1개를 끊은 후, 남은 거리들의 총합을 구하면 된다.
print(sum(dist[:N - K]))
