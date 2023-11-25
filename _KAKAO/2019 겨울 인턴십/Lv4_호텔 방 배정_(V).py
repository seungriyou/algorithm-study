# https://school.programmers.co.kr/learn/courses/30/lessons/64063

def solution(k, room_number):
    room = dict()
    result = []

    for n in room_number:
        # 이미 배정된 방이라면
        if (nrn := room.get(n)):
            # 배정 가능한 방을 찾을 때까지 살펴본 방들을 tracking
            seen = [n]

            # 배정 가능한 방 n_room을 발견할 때까지 반복
            while room.get(nrn):
                seen.append(nrn)
                nrn = room[nrn]

            # 배정 가능한 방을 결과에 추가
            result.append(nrn)

            # 지금까지 살펴본 방들에 대해, 다시 조회된다면 그 다음에 확인할 방 번호 업데이트
            room[nrn] = nrn + 1
            for s in seen:
                room[s] = nrn + 1

        # 배정되지 않은 방이라면
        else:
            # 배정 가능한 방이므로 결과에 추가
            result.append(n)

            # 다시 조회된다면 그 다음에 확인할 방 번호 업데이트
            room[n] = n + 1

    return result
