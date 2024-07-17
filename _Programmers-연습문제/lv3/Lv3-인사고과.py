# https://school.programmers.co.kr/learn/courses/30/lessons/152995

def solution(scores):
    """
    (1차 시도로 for 문을 어떻게 잘 중단시켜보려 했으나 TLE로 실패.. 정렬 + 명제를 적절히 사용해야 한다!)

    ref: https://www.ai-bio.info/programmers/152995

    scores를 이루는 두 점수 (근무 태도 점수, 동료 평가 점수)를 각각 (a, b)라고 할 때, (1) a 기준으로 내림차순 (2) b 기준으로 오름차순 정렬한다.
    이때, 인접한 두 점수의 쌍을 각각 (a1, b1), (a2, b2)라고 해보면 다음과 같은 관계를 가진다.
        (1) a1 >= a2 이다.
        (2) 특히 a1 == a2 라면, b1 <= b2 이다.
    여기에서 (2)번 관계의 대우 "b1 > b2이면, a1 > a2 이다"가 성립함을 알 수 있다.

    따라서 "b1 > b2인 경우"만 발견하면 무조건 "a1 > a2 && b1 > b2가 성립"하는 관계임을 알 수 있으며, 이 경우에는 인센티브를 받지 못한다.
    "a1 > a2 && b1 > b2"인 경우가 한 번이라도 있다면 인센티브를 받지 못하는 것이기 때문에, b1 값은 지금까지 본 "b 값 중 가장 큰 값"이어야 한다.
    그러므로 왼쪽에서부터 max_b 값(b1)을 계속해서 트래킹하고, 현재 b 값(b2)과 비교하여 b1 <= b2인 경우에만 인센티브를 줄 수 있다는 점을 활용한다.
        - 인센티브를 받지 못하는 경우: b1 > b2 (즉, max_b > b)
        - 인센티브를 받는 경우: b1 <= b2 (즉, max_b <= b)

    또한, 완호의 석차만 구하면 되기 때문에 모든 사원을 줄 세울 필요가 없이 완호의 두 점수의 합보다 큰 경우를 모두 세면 된다.
    """

    # 완호의 점수
    target_a, target_b = scores[0]
    target_score = target_a + target_b

    # scores (1) a 기준으로 내림차순 (2) b 기준으로 오름차순 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))

    answer, max_b = 1, -1

    for a, b in scores:
        # 완호가 인센티브를 못 받는 경우
        if a > target_a and b > target_b:
            return -1

        # 인센티브를 받는 경우(b1 <= b2)
        if max_b <= b:
            # "a1 > a2 && b1 > b2"인 경우가 한 번이라도 있다면 인센티브를 받지 못하므로 max_b 값 업데이트
            max_b = b
            # 두 점수의 합이 완호보다 큰 사원들의 수 세기
            if a + b > target_score:
                answer += 1

    return answer
