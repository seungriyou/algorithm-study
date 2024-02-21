# https://school.programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    # total_time: 모든 job들의 작업 요청 ~ 종료까지 걸린 시간의 총합
    # cnt: 완료한 job 개수
    # now: 현재 time
    total_time = cnt = now = 0
    # start: 이전 작업의 시작 time
    start = -1

    # 최소 힙
    q = []

    # 모든 작업을 처리할 때까지
    while cnt < len(jobs):
        for requested_time, required_time in jobs:
            # 요청된 시점이 이전 작업의 시작 시점보다 크고, 현재 시각보다 작거나 같은 경우,
            # 최소 힙에 (1) 작업 소요시간 (2) 작업 요청 시점 우선순위로 넣기
            if start < requested_time <= now:
                heapq.heappush(q, (required_time, requested_time))

        # 처리할 작업이 있다면
        if q:
            required_time, requested_time = heapq.heappop(q)

            # 작업을 새롭게 처리했으므로 start, now, total_time, cnt 업데이트
            start, now = now, now + required_time
            total_time += now - requested_time
            cnt += 1

        # 처리할 작업이 없다면, 현재 시각 now만 증가
        else:
            now += 1

    return total_time // len(jobs)
