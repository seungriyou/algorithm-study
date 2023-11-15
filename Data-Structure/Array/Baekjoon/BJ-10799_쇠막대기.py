# https://www.acmicpc.net/problem/10799
import sys
input = sys.stdin.readline

string = input().rstrip().replace("()", "-").strip("-") # 레이저는 "-"로 변환하고, 맨 끝에 나오는 것은 없애기

stack = []
sticks = 0  # 지금 보고 있는 레이저가 자르고 있는 막대의 개수
answer = 0  # 잘려진 쇠막대기의 총 개수

for s in string:
    # "(" => sticks++ & stack append
    if s == "(":
        stack.append(s)
        sticks += 1

    # ")" => sticks-- & stack pop & 해당 막대기에서 마지막 조각 나옴
    elif s == ")":
        answer += 1    # 1개 만큼의 조각이 생김 (현재 ")"로 마무리된 막대기에서 나온 마지막 조각)
        stack.pop()
        sticks -= 1

    # "-" => 각각의 막대에서마다 조각 +1
    else:   # "-"
        answer += sticks    # 레이저로 인해 sticks 개 만큼의 조각이 생김

print(answer)
