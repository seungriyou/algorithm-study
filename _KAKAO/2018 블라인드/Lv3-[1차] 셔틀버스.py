# https://school.programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    def convert_time_to_int(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    def convert_int_to_time(time):
        h, m = divmod(time, 60)
        return f"{h:02}:{m:02}"

    timetable = sorted([convert_time_to_int(t) for t in timetable])
    start_time = convert_time_to_int("09:00")

    idx = 0  # timetable index
    for _n in range(n):
        # 현재 셔틀의 도착 시각
        curr_time = start_time + _n * t

        # 현재 셔틀에서 curr_time 이전에 도착한 크루 중 최대 m명을 태움
        cnt = 0
        while idx < len(timetable) and timetable[idx] <= curr_time and cnt < m:
            idx += 1
            cnt += 1

        # 마지막 셔틀에서 결정
        if _n == n - 1:
            if cnt < m:
                return convert_int_to_time(curr_time)
            else:
                return convert_int_to_time(timetable[idx - 1] - 1)
