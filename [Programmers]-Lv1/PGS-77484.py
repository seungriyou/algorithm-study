# [PGS] 77484 - 로또의 최고 순위와 최저 순위

from typing import List


def solution(lottos: List[int], win_nums: List[int]) -> List[int]:
    """
    :param lottos: 구매한 로또 번호
    :param win_nums: 당첨 번호
    :return: 당첨 가능한 최고 / 최저 순위를 담은 배열
    """
    # 0 개수
    zeros = lottos.count(0)

    lottos_set = set(lottos)
    win_nums_set = set(win_nums)

    # 일치 번호 개수 2 ~ 6개 = 7 - 개수
    # 일치 번호 개수 0 ~ 1개 = 6
    same_num = len(lottos_set & win_nums_set)

    if same_num < 2 and zeros == 0:
        return [6, 6]
    elif same_num < 2:
        return [7 - same_num - zeros, 6]
    else:
        return [7 - same_num - zeros, 7 - same_num]


lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))
