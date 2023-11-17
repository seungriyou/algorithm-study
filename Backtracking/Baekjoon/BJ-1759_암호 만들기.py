# https://www.acmicpc.net/problem/1759
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
chars = sorted(list(input().split()))

# 암호는 서로 다른 L개의 알파벳 소문자로 구성
# 최소 1 개의 모음 & 최소 2 개의 자음으로 구성
# 증가하는 순서로 정렬

password = []
vowels = set("aeiou")

# v_cnt: password에 포함된 모음 개수, c_cnt: password에 포함된 자음 개수
def backtrack(idx, v_cnt, c_cnt):
    # base condition
    if len(password) == L:
        if v_cnt >= 1 and c_cnt >= 2:
            print("".join(password))
        return

    # recur
    for i in range(idx, C):
        is_vowel = chars[i] in vowels
        password.append(chars[i])
        backtrack(i + 1, v_cnt + is_vowel, c_cnt + (1 - is_vowel))
        password.pop()

backtrack(0, 0, 0)