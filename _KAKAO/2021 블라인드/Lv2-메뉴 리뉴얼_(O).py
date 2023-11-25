# https://school.programmers.co.kr/learn/courses/30/lessons/72411

def solution(orders, course):
    from collections import Counter
    from itertools import combinations

    answer = []

    for c in course:
        candidates = []

        # 각 order에서 가능한 모든 조합 저장
        for order in orders:
            for comb in combinations(sorted(list(order)), c):
                candidates.append("".join(comb))

        # count 후 가장 많이 함께 주문된 순서로 정렬
        counter = Counter(candidates).most_common()

        for menu_set, cnt in counter:
            # 가장 많이 함께 주문했으며, 그 횟수가 2 이상인 단품메뉴 조합만 저장
            if cnt == counter[0][1] and cnt > 1:
                answer.append(menu_set)
            # 위 조건을 만족하지 못했다면 빠르게 종료 (이미 cnt 기준 내림차순 정렬되어 있으므로)
            else:
                break

    answer.sort()  # 사전 순 오름차순 정렬

    return answer
