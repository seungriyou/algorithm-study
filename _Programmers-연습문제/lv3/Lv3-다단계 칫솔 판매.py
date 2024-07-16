# https://school.programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    parents = {child: parent for child, parent in zip(enroll, referral)}

    mapping = {name: i for i, name in enumerate(enroll)}
    result = [0] * len(enroll)

    for name, amnt in zip(seller, amount):
        """
        child == "-"이거나 amnt가 0이 될 때까지 반복:
            - 10% 절사한 amnt 구하기
            - 나머지 90% 떼어서 자기자신 ++
            - child = parents[child] 로 올리기 & amnt를 10% 절사한 값으로 업데이트
        """

        amnt *= 100  # 개당 100원의 이익
        child = name

        while child != "-" and amnt > 0:
            # 10% 절사한 amnt 구하기
            tmp_amnt = amnt // 10

            # 자기자신 이익 챙기기 (나머지)
            result[mapping[child]] += amnt - tmp_amnt

            # 윗 단계로 올리기
            child, amnt = parents[child], tmp_amnt

    return result
