# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
# https://app.codility.com/demo/results/trainingPNRGCC-YB4/

def solution(A):
    # max profit을 얻으려면 매 단계마다...
    # - buy 시점의 가격이 낮아야 하므로 min_price를 트래킹한다.
    # - max_profit을 업데이트 한다.

    max_profit = 0
    min_price = int(1e6)

    for a in A:
        min_price = min(min_price, a)
        max_profit = max(max_profit, a - min_price)

    return max_profit
