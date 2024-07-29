# https://school.programmers.co.kr/learn/courses/30/lessons/150368

def solution(users, emoticons):
    """
    완전 탐색 (itertools) -- faster
    """
    from itertools import product

    res = [0, 0]
    n, m = len(users), len(emoticons)

    ratio_combs = product([10, 20, 30, 40], repeat=m)

    for ratio_comb in ratio_combs:
        comb_res = [0, 0]  # [이모티콘 플러스 가입자, 이모티콘 판매액]
        for ratio, price in users:
            user_price = 0
            for r, e in zip(ratio_comb, emoticons):
                if r >= ratio:
                    user_price += (1 - 0.01 * r) * e

            # 이모티콘 플러스 가입
            if user_price >= price:
                comb_res[0] += 1
            # 이모티콘 구입
            else:
                comb_res[1] += user_price

            res = max(res, comb_res)

    return res


def solution1(users, emoticons):
    """
    완전 탐색 (DFS)
        가능한 이모티콘 할인율의 모든 조합
        res = [이모티콘 플러스 서비스 가입자, 이모티콘 판매액]
    """

    answer = [0, 0]
    m = len(emoticons)
    discounted_emoticons = []  # [(할인율, 이모티콘 가격)]

    def get_register_price(ratio_u, price_u):
        """
        비율 = ratio_u, 가격 = price_u 인 user가 현재 조합의 이모티콘을 구입할 때의
        (이모티콘 플러스 가입 여부, 이모티콘 구매 비용) 반환
        """

        # ratio_u 보다 ratio 높은 이모티콘만 구입할 때의 가격 구하기
        _price = 0
        for ratio, price in discounted_emoticons:
            if ratio_u <= ratio:
                _price += (1 - 0.01 * ratio) * price

        # 이모티콘 플러스 가입
        if _price >= price_u:
            return (True, _price)

        # 이모티콘 구입
        else:
            return (False, _price)

    def dfs(eidx):
        nonlocal answer

        # base condition
        if eidx == m:
            tmp = [0, 0]
            for ratio, price in users:
                # 이모티콘 플러스 가입 여부, 이모티콘 구매 비용
                emoticon_plus, cost = get_register_price(ratio, price)
                # 이모티콘 플러스 가입하는 경우
                if emoticon_plus:
                    tmp[0] += 1
                # 이모티콘 구입하는 경우
                else:
                    tmp[1] += cost

            # 최댓값 업데이트
            if answer < tmp:
                answer = tmp[:]

            return

        # recur
        for i in range(eidx, m):
            for ratio in [10, 20, 30, 40]:
                discounted_emoticons.append((ratio, emoticons[i]))
                dfs(i + 1)
                discounted_emoticons.pop()

    dfs(0)

    return answer
