# https://school.programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    musicinfos = [musicinfo.split(",") for musicinfo in musicinfos]

    def change_note(note):
        # note에서 #를 소문자로 변경하는 함수
        changed_note = note.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#",
                                                                                                                "a")
        return changed_note

    def cal_time(start_time, end_time):
        # 시간 간격을 계산하는 함수 (분 단위)
        sh, sm = map(int, start_time.split(":"))
        eh, em = map(int, end_time.split(":"))

        total_time = (eh - sh) * 60 + (em - sm)

        return total_time

    def get_played_note(total_time, splitted_note):
        # 실제 주어진 시간동안 재생된 note로 이루어진 리스트를 반환하는 함수
        n = len(splitted_note)

        if total_time <= n:
            return splitted_note[:total_time]
        else:
            d, m = divmod(total_time, n)
            return splitted_note * d + splitted_note[:m]

    m = change_note(m)

    # 최대 재생 시간 tracking
    max_total_time = 0
    answer = "(None)"

    for info in musicinfos:
        # info 파싱
        start_time, end_time, title, note = info
        # 재생 시간 계산
        total_time = cal_time(start_time, end_time)
        # note 변환
        changed_note = change_note(note)
        # 실제 재생된 note
        played_note = get_played_note(total_time, changed_note)

        if m in played_note:
            # 재생 시간 업데이트
            if total_time > max_total_time:
                max_total_time = total_time
                answer = title

    return answer


# ===== 첫 번째 풀이 =====
def solution2(m, musicinfos):
    musicinfos = [musicinfo.split(",") for musicinfo in musicinfos]

    def split_note(notes):
        # note를 parsing 하는 함수
        i = 0
        result = []
        n = len(notes)

        while i < n:
            if i + 1 < n and notes[i + 1] == "#":
                result.append(notes[i:i + 2])
                i += 2
            else:
                result.append(notes[i])
                i += 1

        return result

    def cal_time(start_time, end_time):
        # 시간 간격을 계산하는 함수 (분 단위)
        sh, sm = map(int, start_time.split(":"))
        eh, em = map(int, end_time.split(":"))

        total_time = (eh - sh) * 60 + (em - sm)

        return total_time

    def get_played_note(total_time, splitted_note):
        # 실제 주어진 시간동안 재생된 note로 이루어진 리스트를 반환하는 함수
        n = len(splitted_note)

        if total_time < n:
            return splitted_note[:total_time]
        else:
            d, m = divmod(total_time, n)
            return splitted_note * d + splitted_note[:m]

    m = split_note(m)

    result = []

    for i, info in enumerate(musicinfos):
        # info 파싱
        start_time, end_time, title, note = info
        # 재생 시간 계산
        total_time = cal_time(start_time, end_time)
        # note parsing
        splitted_note = split_note(note)
        # 실제 재생된 note
        played_note = get_played_note(total_time, splitted_note)

        for j in range(len(m), len(played_note) + 1):
            # m과 같은 구간이 played_note에서 발견되면 result에 우선순위를 고려하여 tuple로 추가
            if m == played_note[j - len(m):j]:
                result.append((-total_time, i, title))
                break

    if result:
        # 우선순위대로 정렬 (재생 시간 DESC, 입력 순서 ASC)
        result.sort()
        return result[0][2]

    else:
        return "(None)"  # 없으면 None 반환
