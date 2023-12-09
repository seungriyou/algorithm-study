# https://www.acmicpc.net/problem/20546
import sys
input = sys.stdin.readline

cash = int(input())
stocks = list(map(int, input().split()))

jh_cash = sm_cash = cash
jh_stock = sm_stock = 0
record = 0

for i, stock in enumerate(stocks):
    # 준현
    buy = jh_cash // stock
    jh_cash -= stock * buy
    jh_stock += buy

    # 성민
    if i == 0:
        continue

    if stocks[i - 1] < stocks[i]:
        if record < 0:
            record = 1
        else:
            if record >= 2:
                # 전량 매도
                sm_cash += sm_stock * stock
                sm_stock = 0
            record += 1

    elif stocks[i - 1] > stocks[i]:
        if record > 0:
            record = -1
        else:
            if record <= -2:
                # 전량 매수
                buy = sm_cash // stock
                sm_cash -= stock * buy
                sm_stock += buy
            record -= 1

    else:
        record = 0


jh = jh_cash + stocks[-1] * jh_stock
sm = sm_cash + stocks[-1] * sm_stock
if jh > sm:
    print("BNP")
elif jh < sm:
    print("TIMING")
else:
    print("SAMESAME")
