# https://school.programmers.co.kr/learn/courses/30/lessons/12920

def solution(n, cores):
    """parametric search
    ref: https://gkalstn000.github.io/2021/03/01/%EC%84%A0%EC%9E%85-%EC%84%A0%EC%B6%9C-%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81/

    시간 별로 각 core에서 처리되는 작업의 개수는 각각 다음과 같으며, t(h)까지 처리되는 작업의 총 개수를 수식으로 구할 수 있다.

    cores   |   1   |   2   |   3
    -------- ------- ------- -------
    0(h)    |   1   |   1   |   1
    1(h)    |   1   |       |
    2(h)    |   1   |   1   |
    ...     |  ...  |  ...  |  ...
    -------- ------- ------- -------
    t(h) 총합| t/1+1 | t/2+1 | t/3+1
    """

    # 코어의 개수
    m = len(cores)

    # 작업의 개수가 코어의 개수보다 같거나 작으면 n 반환
    if n <= m:
        return n

    # 작업의 개수가 코어의 개수보다 크면 n에서 m만큼 빼기 (t(h)에서 +1 부분 미리 제외)
    n -= m

    # 이분탐색을 통해 마지막 작업까지 모두 완료되는 데까지 필요한 시간 time 구하기
    lo, hi = min(cores) * n // m, max(cores) * n // m
    time = 0

    def get_done_tasks(time):
        return sum(time // core for core in cores)

    while lo <= hi:
        mid = (lo + hi) // 2

        if get_done_tasks(mid) >= n:
            time = mid
            hi = mid - 1
        else:
            lo = mid + 1

    # time - 1 시간 까지는 모든 core에서 작업 진행
    n -= sum((time - 1) // core for core in cores)

    # time 시간에서는 마지막 작업이 진행되는 core 번호를 찾기
    for i, core in enumerate(cores, start=1):
        # time 시간에 core에서 작업을 수행할 수 있다면 n--
        if time % core == 0:
            n -= 1
        # n == 0이라면 종료
        if not n:
            return i


def solution_tle(n, cores):
    """TLE (tc 4,5,6)"""
    import heapq

    if len(cores) >= n:
        return n

    q = [(core, i + 1) for i, core in enumerate(cores)]  # 최소 힙: [(작업 마무리 시간, 코어 번호)]
    heapq.heapify(q)
    n -= len(cores)

    # 작업이 1개 남을 때까지 반복
    while n > 1:
        # 작업이 완료된 코어의 (이전 작업 마무리 시간, 코어 번호) pop
        time, num = heapq.heappop(q)
        # pop 한 코어에 새로운 작업 부여
        heapq.heappush(q, (time + cores[num - 1], num))
        # 남은 작업 개수 --
        n -= 1

    # 마지막 작업을 수행하는 코어 번호 반환
    return q[0][1]
