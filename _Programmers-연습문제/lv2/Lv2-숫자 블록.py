# https://school.programmers.co.kr/learn/courses/30/lessons/12923

def solution(begin, end):
    """
    각 숫자의 "최대 약수"를 구하면 된다. (단, 자기자신 제외)
    """
    answer = []

    def get_max_divisor(num):
        if num == 1:
            return 0

        max_divisor = 1

        for i in range(2, int(num ** 0.5) + 1):
            q, r = divmod(num, i)

            # i가 num의 약수가 아니라면 넘어가기
            if r != 0:
                continue

            # 보고 있는 약수 쌍 (i, q)는 i <= q
            # i == q인 경우는 최대 sqrt(1e9) 일 때이므로 1e7 보다 작음
            # i < q인 경우에는, q가 1e7 보다 같거나 작을 때에만 반영해야 함
            if q <= 1e7:
                max_divisor = max(max_divisor, q)
                break  # *** 어차피 제일 먼저 찾은 q가 가장 큰 값이 될 것이므로 여기서 끊어줘야 효율성 체크 통과 가능!
            else:
                max_divisor = max(max_divisor, i)

        return max_divisor

    for n in range(begin, end + 1):
        answer.append(get_max_divisor(n))

    return answer
