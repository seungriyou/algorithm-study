# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
from math import ceil


def solution(fees, records):
    LAST_MIN = 23 * 60 + 59
    answer = []

    base_time, base_fee, unit_time, unit_fee = fees

    r_dict = defaultdict(lambda: {"IN": [], "OUT": []})

    for record in records:
        hhmm, car_num, des = record.split()
        h, m = map(int, hhmm.split(":"))
        mm = h * 60 + m  # 00:00 부터 해당 시각까지의 시간을 분 단위로
        r_dict[car_num][des].append(mm)

    total_time = dict()
    for car_num, record in r_dict.items():
        tot_time = 0
        for i, o in zip(record["IN"], record["OUT"]):
            tot_time += o - i
        if len(record["OUT"]) < len(record["IN"]):  # 입차는 되었으나 출차 기록이 없는 경우
            tot_time += LAST_MIN - record["IN"][-1]  # 23:59 출차로 가정
        total_time[car_num] = tot_time

    for car_num in sorted(total_time.keys()):  # 차량 번호 오름차순 정렬
        tot_time = total_time[car_num]
        if tot_time <= base_time:
            answer.append(base_fee)
        else:
            answer.append(base_fee + ceil((tot_time - base_time) / unit_time) * unit_fee)

    return answer
