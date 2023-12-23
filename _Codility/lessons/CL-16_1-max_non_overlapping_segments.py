# https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/
# https://app.codility.com/demo/results/trainingW4FFG7-CG8/
# BJ-1931 회의실 배정(https://www.acmicpc.net/problem/1931) 문제와 비슷

def solution(A, B):
    # 오름차순 정렬 우선순위: end -> start
    segments = sorted(list(zip(A, B)), key=lambda x: (x[1], x[0]))
    cnt = 0
    last_end = -1

    for s, e in segments:
        if s > last_end:
            cnt += 1
            last_end = e

    return cnt
