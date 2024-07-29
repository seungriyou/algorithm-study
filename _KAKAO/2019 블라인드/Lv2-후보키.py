# https://school.programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations


def solution(relation):
    """
    - 가능한 조합 모두 모으기
    - subset이 존재하는 것 제거
    """

    row, col = len(relation), len(relation[0])
    relation_t = list(zip(*relation))  # transposed relation
    res = []

    # 1 ~ col 개 조합 구하기
    for i in range(1, col + 1):
        for comb in combinations(range(col), i):
            # [유일성] 해당 column 조합이 unique 한 경우
            comb_cols = set(zip(*[relation_t[j] for j in comb]))
            if len(comb_cols) == row:
                # [최소성] 이전에 담은 unique 한 조합과 하나라도 겹친다면 res에 담지 X
                for u_comb in res:
                    if u_comb.issubset(set(comb)):
                        break
                # 이전에 담은 unique 한 조합과 겹치는 것이 없다면 res에 담기
                else:
                    res.append(set(comb))

    return len(res)
