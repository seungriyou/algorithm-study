# [PGS] 92334 - 신고 결과 받기

from typing import List
from collections import defaultdict


def solution(id_list: List[str], report: List[str], k: int) -> List[int]:
    """
    :param id_list: 이용자의 ID가 담긴 문자열 배열
    :param report: 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열
    :param k: 정지 기준이 되는 신고 횟수
    :return: 각 유저별로 처리 결과 메일을 받은 횟수를 담은 배열
    """

    id_idx = {user: i for i, user in enumerate(id_list)}
    # pairs = [(이용자id, 신고한id)]
    pairs = [tuple(pair.split()) for pair in report]
    # report_dict = { rcv1 : {snd1, snd2, ...}, }
    report_dict = defaultdict(set)  # {user: set() for user in id_list}
    for pair in pairs:
        report_dict[pair[1]].add(pair[0])

    result = [0] * len(id_list)

    # 리스트의 길이 >= k인 경우, 각 신고자에게 메일 발송
    for rcv, snds in report_dict.items():
        if len(snds) >= k:
            for snd in snds:
                result[id_idx[snd]] += 1

    return result


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))
