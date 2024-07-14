# https://school.programmers.co.kr/learn/courses/30/lessons/155651

import heapq


def solution(book_time):
    # (시작, 끝+10분)
    def plus_ten_min(start, end):
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        return (sh * 60 + sm, eh * 60 + em + 10)

    times = [plus_ten_min(start, end) for start, end in book_time]

    # start 시간 이른 순으로 정렬
    times.sort()

    # end 시간 기준 최소힙 구성
    q = []

    for start, end in times:
        # 현재 보고 있는 start >= q[0](= 가장 빨리 마치는 end) 인 경우, 해당 객실을 이어서 사용할 수 있음
        if q and start >= q[0]:
            heapq.heappop(q)

        # 현재 보고 있는 end 기록하기
        heapq.heappush(q, end)

    return len(q)
