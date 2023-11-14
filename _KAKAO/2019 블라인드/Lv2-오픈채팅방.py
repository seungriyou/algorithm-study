# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []

    # user 별 last username 기록
    last_username = dict()
    for r in record:
        tmp = r.split()
        action, uid = tmp[0], tmp[1]
        if action != "Leave":
            last_username[uid] = tmp[2]

    for r in record:
        tmp = r.split()
        action, uid = tmp[0], tmp[1]

        if action == "Enter":
            answer.append(f"{last_username[uid]}님이 들어왔습니다.")

        elif action == "Leave":
            answer.append(f"{last_username[uid]}님이 나갔습니다.")

    return answer
