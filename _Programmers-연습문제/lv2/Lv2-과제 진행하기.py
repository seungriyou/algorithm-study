# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    """
    - plans (start 순으로 오름차순 정렬): 새로운 과제
    - stack: 진행 중인 과제 ([과제 이름, 남은 시간])

    과제를 끝낸 순서대로 이름을 배열에 담아 반환
    """

    def convert_to_min(hhmm):
        h, m = map(int, hhmm.split(":"))
        return h * 60 + m

    answer = []
    stack = []

    # start 기준으로 오름차순 정렬
    plans = sorted(
        [(name, convert_to_min(start), int(playtime)) for name, start, playtime in plans],
        key=lambda x: x[1]
    )
    # 현재 시각 (= 마지막 확인 시각)
    curr = plans[0][1]

    for name, start, playtime in plans:
        # 진행 중인 과제가 있고, 현재 시각(= 마지막 확인 시각)이 start 보다 작은 경우
        while stack and curr < start:
            # 최근 진행 중 과제를 완전 완료할 수 있는 경우
            if (new_end := curr + stack[-1][1]) <= start:
                answer.append(stack.pop()[0])
                curr = new_end
            # 최근 진행 중 과제를 부분 완료할 수 있는 경우
            else:
                stack[-1][1] = new_end - start
                break

        # 현재 새롭게 보고 있는 과제를 진행 중 과제에 등록
        stack.append([name, playtime])

        # 현재 시각(= 마지막 확인 시각) 업데이트 (**주의**)
        # stack에 있었던 과제들을 모두 완료한 경우에도 curr를 업데이트해주기 위함
        curr = start

    # 아직 진행 중인 과제를 최근 추가된 순으로 마치기
    while stack:
        answer.append(stack.pop()[0])

    return answer
