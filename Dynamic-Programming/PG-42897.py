# [PG] 42897 - 도둑질 (Lv4)
# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    """
    i 번째 집을 볼 때, 가장 많이 훔칠 수 있는 돈의 금액
    dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
                -> prev1    -> prev2

    인접한 두 집 털면 안되므로, 양 끝집이 둘 다 털리면 X
    -> 양 끝집을 하나씩 빼면서 dp 진행해보고, 그 중에서 최댓값을 반환하도록 함
    """

    prev1 = prev2 = 0
    max1 = max2 = 0

    # 맨 마지막 집 제외
    for i in range(len(money) - 1):
        max1 = max(prev1, prev2 + money[i])
        prev2, prev1 = prev1, max1

    prev1 = prev2 = 0

    # 맨 첫번째 집 제외
    for i in range(1, len(money)):
        max2 = max(prev1, prev2 + money[i])
        prev2, prev1 = prev1, max2

    return max(max1, max2)


money = [1, 2, 3, 1]
assert 4 == solution(money)
