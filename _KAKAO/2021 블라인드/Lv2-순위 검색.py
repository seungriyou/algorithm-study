# https://school.programmers.co.kr/learn/courses/30/lessons/72412

def solution(info, query):
    """
    전체 조합 미리 구하기 + (dictionary & simpler binary search)
    """
    from collections import defaultdict

    answer = []
    combs = defaultdict(list)

    # info
    for i, inf in enumerate(info):
        lang, pos, exp, food, score = inf.split()
        # 현재 사람이 속할 수 있는 16가지 조합에 점수 기록
        for i in {"-", lang}:
            for j in {"-", pos}:
                for k in {"-", exp}:
                    for l in {"-", food}:
                        combs[(i, j, k, l)].append(int(score))

    # score 정렬하기
    for comb in combs:
        combs[comb].sort()

    # 이분탐색으로 score_list에서 score 이상인 값의 개수 반환하는 함수 작성하기[**주의**]
    def get_number_of_ge_scores(score, score_list):
        left, right = 0, len(score_list)

        while left < right:
            mid = (left + right) // 2
            if score_list[mid] >= score:
                right = mid
            else:
                left = mid + 1

        return len(score_list) - right

    # query
    for q in query:
        i, j, k, l, score = q.replace(" and ", " ").split()
        answer.append(get_number_of_ge_scores(int(score), combs[(i, j, k, l)]))

    return answer


def solution1(info, query):
    """
    전체 조합 미리 구하기

    한 사람당 16개의 조합에 속할 수 있다.
        언어(O / -) * 직급(O / -) * 경력(O / -) * 소울푸드(O / -) = 2 * 2 * 2 * 2 = 16

    모든 조합은
        언어(3 + 1(-)) * 직급(2 + 1(-)) * 경력(2 + 1(-)) * 소울푸드(2 + 1(-)) = 4 * 3 * 3 * 3 = 36가지 이다.

    각 조합마다 속하는 점수들을 모으고, 정렬하고, 이분탐색 하면 된다.
    """
    answer = []
    combs = [[[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)]
    lang_map = {"-": 0, "cpp": 1, "java": 2, "python": 3}
    pos_map = {"-": 0, "backend": 1, "frontend": 2}
    exp_map = {"-": 0, "junior": 1, "senior": 2}
    food_map = {"-": 0, "chicken": 1, "pizza": 2}

    # info
    for i, inf in enumerate(info):
        lang, pos, exp, food, score = inf.split()
        # 현재 사람이 속할 수 있는 16가지 조합에 점수 기록
        for i in {"-", lang}:
            for j in {"-", pos}:
                for k in {"-", exp}:
                    for l in {"-", food}:
                        combs[lang_map[i]][pos_map[j]][exp_map[k]][food_map[l]].append(int(score))

    # score 정렬하기
    for i in range(4):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    combs[i][j][k][l].sort()

    # 이분탐색으로 score_list에서 score 이상인 값의 개수 반환하는 함수 작성하기[**주의**]
    def get_number_of_ge_scores(score, score_list):
        # score_list가 비어있는 경우 0 반환
        if not score_list:
            return 0

        # score가 scores의 범위를 벗어나는 경우 핸들링
        if score < score_list[0]:
            return len(score_list)
        elif score > score_list[-1]:
            return 0

        # score가 scores의 범위에 속하는 경우 이분 탐색
        left, right = 0, len(score_list) - 1
        boundary = 0

        while left <= right:
            mid = (left + right) // 2
            if score_list[mid] >= score:
                boundary = mid
                right = mid - 1
            else:
                left = mid + 1

        return len(score_list) - boundary

    # query
    for q in query:
        i, j, k, l, score = q.replace(" and ", " ").split()
        answer.append(get_number_of_ge_scores(int(score), combs[lang_map[i]][pos_map[j]][exp_map[k]][food_map[l]]))

    return answer


def solution_tle(info, query):
    """TLE :(
    info
        - 3 가지 구분 내의 옵션 별로 집합 구성
        - 부분집합으로 구하기
        - 마지막 숫자는 점수 X이므로 binary search로 찾도록?
    query
        - " and "로 split
        - "-"이면 넘어가기
        - 마지막은 숫자
    """
    answer = []

    language = {"cpp": set(), "java": set(), "python": set()}
    position = {"backend": set(), "frontend": set()}
    experience = {"junior": set(), "senior": set()}
    soul_food = {"chicken": set(), "pizza": set()}
    scores = []

    def get_ge_scores(score):
        left, right = 0, len(scores) - 1
        boundary = 0

        # score가 scores의 범위를 벗어나는 경우 핸들링
        if score < scores[0][0]:
            boundary = 0
        elif score > scores[-1][0]:
            boundary = len(scores)
        # score가 scores의 범위에 속하는 경우 이분 탐색
        else:
            while left <= right:
                mid = (left + right) // 2
                if scores[mid][0] >= score:
                    boundary = mid
                    right = mid - 1
                else:
                    left = mid + 1

        return set(scores[i][1] for i in range(boundary, len(scores)))

    # info
    for i, inf in enumerate(info):
        lang, pos, exp, food, score = inf.split()
        language[lang].add(i)
        position[pos].add(i)
        experience[exp].add(i)
        soul_food[food].add(i)
        scores.append((int(score), i))

    scores.sort()

    # query
    for q in query:
        cnt = 0
        *condition, score = q.replace(" and ", " ").split()
        # *condition, score = q.split()

        # 조건
        lang, pos, exp, food = condition
        tmp = set(range(len(info)))
        if lang != "-":
            tmp &= language[lang]
        if pos != "-":
            tmp &= position[pos]
        if exp != "-":
            tmp &= experience[exp]
        if food != "-":
            tmp &= soul_food[food]

        # 코딩테스트 점수
        answer.append(len(tmp & get_ge_scores(int(score))))

    return answer
