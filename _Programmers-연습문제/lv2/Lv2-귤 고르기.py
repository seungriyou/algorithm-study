# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    # 귤의 크기의 최대값
    max_size = max(tangerine)

    # index가 (귤의 크기 - 1)인 배열 생성
    cnt_per_size = [0] * max_size

    # 귤 크기 별 개수 세기
    for t in tangerine:
        cnt_per_size[t - 1] += 1

    # 개수 기준, 내림차순 정렬
    cnt_per_size.sort(reverse=True)

    # 개수가 많은 크기부터 세어가면서, k 이상인 순간에 해당 index + 1을 반환
    cnt = 0
    for i in range(max_size):
        cnt += cnt_per_size[i]
        if cnt >= k:
            return i + 1

    return max_size
