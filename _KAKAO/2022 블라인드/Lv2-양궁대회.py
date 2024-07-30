# https://school.programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    """
    backtracking

    - 과녁판의 각 점수 k에 대해 어피치가 a발, 라이언이 b발을 맞혔다면,
        - a == b == 0: 아무도 k점을 가져가지 않음
        - a >= b: 어피치가 +k점
        - a < b: 라이언이 +k점
    - 최종 점수가 더 높은 선수를 우승자로 결정
        - 최종 점수가 같을 경우 어피치를 우승자로 결정
    -   (1) 라이언이 어피치를 가장 큰 점수 차이로 이기기 위해 n발의 화살을 어떤 점수에 맞혀야 할지
        (2) 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지라면, 가장 낮은 점수를 더 많이 맞힌 경우 반환

    - 라이언이 무조건 지거나 비기는 경우는 [-1] 반환
    """

    answer = [-1]
    max_score_diff = 0
    ryan = [0] * 11

    def get_ryan_apeach_diff():
        score_diff = 0
        for i, (a, r) in enumerate(zip(info, ryan)):
            if a >= r and a != 0:
                score_diff -= 10 - i
            elif a < r:
                score_diff += 10 - i

        # <= 0이라면 어피치 승, > 0이라면 라이언 승
        return score_diff

    def to_be_updated(score_diff):
        # (1) 가장 큰 점수 차이이거나, (2) 점수 차이가 같다면 가장 낮은 점수를 더 많이 맞혔는지 확인 후 업데이트
        return (score_diff > max_score_diff) or (score_diff == max_score_diff and ryan[::-1] > answer[::-1])

    def backtrack(n, idx):
        """
        recur 시, (1) k점을 어피치보다 많이 맞혔거나 (2) k점을 맞히지 않는 경우를 모두 확인
        base condition에서 남은 화살 개수를 ryan[10]에 반영
        """
        nonlocal answer, max_score_diff

        # base condition
        if n == 0 or idx == 11:
            # 라이언이 이긴 경우
            if (score_diff := get_ryan_apeach_diff()) > 0:
                # 남은 화살 개수 반영
                if n >= 0:
                    ryan[10] = n
                # 업데이트
                if to_be_updated(score_diff):
                    answer = ryan[:]
                    max_score_diff = score_diff
            return

        # recur
        # (1) 10 - idx 점을 어피치보다 1번 더 많이 맞히는 경우
        if n > info[idx]:
            cnt = info[idx] + 1
            ryan[idx] = cnt
            backtrack(n - cnt, idx + 1)
            ryan[idx] = 0

        # (2) 10 - idx 점을 맞히지 않는 경우
        backtrack(n, idx + 1)

    backtrack(n, 0)

    return answer
